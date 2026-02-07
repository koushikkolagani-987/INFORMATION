import os
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def extract_text_from_pdfs(pdf_docs):
    """
    Extract text from uploaded PDF files
    """
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def process_text(text):
    """
    Send extracted text to Gemini and get response
    """
    if not text.strip():
        return "No readable text found in the PDFs."

    model = genai.get_model("models/gemini-pro")

    prompt = f"""
    You are an intelligent document analyzer.
    Read the following document content and give:
    1. A short summary
    2. Key points
    3. Important insights

    Document:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text
