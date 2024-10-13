import os
from typing import List
from langchain_core.documents import Document 
from langchain.document_loaders import PyPDFLoader

def load(directory:str = "data") -> List[Document]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    root_dir = os.path.join(script_dir, "..", directory)
    data_dir = os.path.abspath(root_dir)

    pdf_documents = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".pdf")]

    loaders = [PyPDFLoader(doc) for doc in pdf_documents]

    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    
    print(len(docs))
    return docs

if __name__ == "__main__":
    load("data")
