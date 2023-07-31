from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader('scraped_text.txt')
docs = loader.load()
char_text_splitter = CharacterTextSplitter(chunk_size = 2000, chunk_overlap = 0)
doc_texts = char_text_splitter.split_documents(docs)


EMBEDDING_MODEL = "text-embedding-ada-002"
embeddings = OpenAIEmbeddings(openai_api_key='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')

pinecone.init(
    api_key="4a6b51e2-8b29-4f38-b6c0-5be6ebf5f5ed",
    environment="us-central1-gcp"
)

index_name = "test"

doc_store = Pinecone.from_texts([d.page_content for d in doc_texts],embeddings,index_name=index_name)
query = "What is the history of web scraping?"
docs = doc_store.similarity_search(query)
print(docs[0].page_content[:])