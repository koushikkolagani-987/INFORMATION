import os
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def extract_text_from_pdfs(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def process_text(text):
    if not text.strip():
        return "No readable text found in the PDFs."

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Analyze the following document and provide:
    - Summary
    - Key points
    - Important insights

    Document:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
