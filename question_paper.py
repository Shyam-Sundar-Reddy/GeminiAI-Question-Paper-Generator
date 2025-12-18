import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from PyPDF2 import PdfReader
import docx
from fpdf import FPDF
import datetime

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "it-assistant-chat"

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in .env")
    st.stop()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Question Paper Generator", layout="centered")
st.title("📝 AI Question Paper Generator")
st.markdown("""
Upload a document, and generate a question paper with answers automatically.
- Supported file types: PDF, DOC, DOCX, TXT
- Set number of questions, average answer length, and difficulty
""")

# -----------------------------
# File upload
# -----------------------------
uploaded_file = st.file_uploader("Upload your document", type=["pdf", "doc", "docx", "txt"])
file_text = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            file_text += page.extract_text()
    elif uploaded_file.type in ["application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            file_text += para.text + "\n"
    elif uploaded_file.type == "text/plain":
        file_text = uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file type")

# -----------------------------
# User inputs
# -----------------------------
num_questions = st.number_input("Number of questions", min_value=1, max_value=50, value=10)
avg_answer_len = st.number_input("Average answer length (words)", min_value=10, max_value=500, value=50)
difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard", "Very Hard"])

# -----------------------------
# LangChain prompt setup
# -----------------------------
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert exam generator. Generate questions and answers clearly and concisely."
    ),
    (
        "user",
        "{question}"
    )
])

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.6,
    google_api_key=GOOGLE_API_KEY
)

chain = prompt_template | llm | StrOutputParser()

# -----------------------------
# Generate Q&A
# -----------------------------
if uploaded_file:
    generate_button = st.button("Generate Question Paper")
    if generate_button:
        if not file_text.strip():
            st.error("No text found in uploaded file")
        else:
            question_prompt = f"""
            From the following text, generate {num_questions} questions with answers.
            Difficulty: {difficulty}
            Average answer length: {avg_answer_len} words.
            Text:
            {file_text}
            """
            with st.spinner("Generating questions and answers..."):
                qna_response = chain.invoke({"question": question_prompt})

            st.markdown("### Generated Questions & Answers")
            st.text_area("Q&A", qna_response, height=400)

            # -----------------------------
            # Export to PDF
            # -----------------------------
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 6, qna_response)

            filename = f"QuestionPaper_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            pdf.output(filename)

            st.success("PDF generated successfully!")
            st.download_button("Download PDF", filename, file_name=filename)
