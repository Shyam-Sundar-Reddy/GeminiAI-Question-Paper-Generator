# 📝 AI Question Paper Generator

An AI-powered **Question Paper Generator** built with **Streamlit**, **LangChain**, and **Google Gemini**. Upload study material (PDF, DOC/DOCX, TXT) and automatically generate exam-style questions with answers. Export the results as a downloadable **PDF**.

---

## 🚀 Features

* 📄 Upload documents: **PDF, DOC, DOCX, TXT**
* 🤖 AI-generated **questions & answers**
* 🎯 Configurable:

  * Number of questions
  * Difficulty level (Easy → Very Hard)
  * Average answer length
* 📑 Export generated Q&A as **PDF**
* 🔍 LangChain tracing enabled for observability
* ⚡ Fast and interactive **Streamlit UI**

---

## 🧠 Tech Stack

* **Python 3.9+**
* **Streamlit** – UI
* **LangChain** – Prompt orchestration
* **Google Gemini (gemini-2.0-flash)** – LLM
* **PyPDF2** – PDF text extraction
* **python-docx** – DOC/DOCX parsing
* **FPDF** – PDF generation
* **dotenv** – Environment management

---

## 📂 Project Structure

```text
.
├── app.py                  # Main Streamlit application
├── .env                    # Environment variables (not committed)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

> ⚠️ Never commit `.env` files to GitHub

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ai-question-paper-generator.git
cd ai-question-paper-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🧪 How It Works

1. Upload a document
2. Text is extracted based on file type
3. User selects question count, difficulty, and answer length
4. LangChain sends structured prompt to Gemini
5. AI generates questions and answers
6. Output is displayed and exported as PDF

---

## 📘 Example Use Cases

* Teachers creating exam papers
* Students preparing mock tests
* Training institutes
* Corporate assessment creation
* Interview question generation

---

## 📈 Future Improvements

* Token limit handling with chunking
* Question types (MCQ, descriptive, coding)
* Bloom’s taxonomy-based questions
* Answer key only / question-only export
* Multiple document uploads
* AWS / GCP deployment

---

## 🛡️ Observability

LangChain tracing is enabled:

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "it-assistant-chat"
```

Monitor executions in **LangSmith Dashboard**.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---


* LangChain
* Google Generative AI (Gemini)
* Streamlit Community
