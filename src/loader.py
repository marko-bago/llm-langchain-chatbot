import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_data():

    # Load, chunk and index the contents of the blog.
    loader = WebBaseLoader(
        web_paths=("https://www.index.hr/vijesti/clanak/oglasio-se-milanovic-objavio-planove-ako-mi-hdzovi-ustavni-suci-zabrane/2548111.aspx?index_ref=naslovnica_vijesti_prva_d",)
    )

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    return splits

if __name__ == "__main__":
    splits = load_data()
    print(splits)