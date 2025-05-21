# RAG PDF Question Answering App

This is a local Retrieval-Augmented Generation (RAG) application that allows you to upload PDF documents and ask questions about their content.


Clone the repository and install dependencies

```bash
git clone https://github.com/Girishchouhan008/RAG_pdf_test.git


python -m venv env
env\Scripts\activate


cd rag_pdf_test
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
pip install sklearn
pip install streamlit

python download_model.py

streamlit run app.py

 -->
