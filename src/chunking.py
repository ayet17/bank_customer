from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunker(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1500,
        chunk_overlap = 150
    )
    splits = text_splitter.split_documents(docs)
    return splits
