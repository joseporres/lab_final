from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from langchain.document_loaders import TextLoader
from app.config.settings import api_settings

API_KEY = api_settings.OPEN_AI_KEY
persist_directory='vectordb'

embeddings = OpenAIEmbeddings(
    api_key=API_KEY
)

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
qa = VectorDBQA.from_chain_type(llm=OpenAI(
    api_key=API_KEY,
), chain_type="stuff", vectorstore=vectordb)