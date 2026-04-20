from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]

Settings.llm = OpenAI(model="gpt-4o", temperature=0.1, api_key=api_key)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small", api_key=api_key)

documents = SimpleDirectoryReader("./history_pages").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(similarity_top_k=10)