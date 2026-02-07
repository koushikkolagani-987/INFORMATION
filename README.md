# INFORMATION
reads the given file and gives you the output
# 📄 Information System – PDF Analysis using Gemini AI

## 🔍 Project Overview
This project is a **Streamlit-based web application** that allows users to upload PDF documents and extract meaningful information such as:
- Document summary
- Key points
- Important insights

The system is designed to demonstrate how **Generative AI (Google Gemini)** can be integrated with Python to analyze documents.

---

## 🛠️ Tech Stack
- **Python 3.10**
- **Streamlit** – Web interface
- **PyPDF2** – PDF text extraction
- **Google Gemini API** – Generative AI model
- **python-dotenv** – Environment variable management
- **FAISS (planned)** – Vector database for RAG (future scope)

---

## 📁 Project Structure


---

## ▶️ How the Application Works
1. User uploads one or more PDF files.
2. Text is extracted from PDFs using PyPDF2.
3. Extracted text is sent to Google Gemini for analysis.
4. The AI-generated output is displayed on the web interface.

---

## ⚠️ Current Limitation (Important Note)
This project **may not run end-to-end at present** due to **recent breaking changes and restrictions in Google Gemini APIs**:

- Several Gemini models (`gemini-pro`, earlier `v1beta` endpoints) have been deprecated or restricted.
- Older and newer SDKs (`google-generativeai`, `google-genai`) behave differently.
- Some models are not accessible depending on API version, region, or account permissions.

As a result, **model availability errors (404 / not supported)** may occur even with correct code.

---

## 🎯 Why This Project Is Still Valuable
- Demonstrates **real-world GenAI integration challenges**
- Shows **modular project design** (UI + backend separation)
- Highlights ability to **adapt to rapidly changing APIs**
- Reflects industry reality where third-party services change frequently

The project logic, structure, and intent remain correct and production-oriented.

---

## 🚀 Future Improvements
- Replace Gemini with a stable LLM provider (OpenAI / Azure / local LLM)
- Implement **RAG pipeline** using FAISS
- Add **document Q&A chatbot**
- Deploy on Streamlit Cloud / Hugging Face Spaces

---

## 🧑‍💻 Author
**Koushik Kolagani**  
B.Tech CSE | AI & ML Enthusiast  
Focused on Data Analytics, GenAI, and Full-Stack AI Projects

---

## 📌 Disclaimer
This project is intended for **educational and demonstration purposes**.  
API availability depends on third-party providers and may change over time.
