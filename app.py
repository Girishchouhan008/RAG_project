import streamlit as st
import os
import fitz  
from rag import get_answer

st.set_page_config(page_title="RAG PDF Chat", layout="wide")

st.title("Upload your PDF file Only")
st.write("Upload a PDF and ask questions about its content.")


uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    os.makedirs("uploaded_pdfs", exist_ok=True)

    # Save pdf file
    file_path = f"uploaded_pdfs/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # PDF name
    st.success(f"Uploaded: {uploaded_file.name}")

    # Extract from pdf
    with fitz.open(file_path) as doc:
        pdf_text = ""
        for page in doc:
            pdf_text += page.get_text()

    st.subheader("Ask a question about the PDF")
    question = st.text_input("Your question")

    if question:
        with st.spinner("Searching..."):
            answer = get_answer(question, pdf_text)
        st.markdown(f"**Answer:** {answer}")
