import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]

Settings.llm = OpenAI(
        model="gpt-4o", 
        temperature=0.1, 
        api_key=api_key
        )
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small", 
    api_key=api_key
    )

@st.cache_resource
def load_index():
    documents = SimpleDirectoryReader("./history_pages").load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index


index = load_index()
qa_prompt = PromptTemplate(
    "You are an Islamic History assistant.\n"
    "Use the provided context as the primary source of truth.\n"
    "Handle spelling variations of names.\n"
    "If the answer is not in the context, say you do not have enough information.\n\n"
    "Context:\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n\n"
    "Question: {query_str}\n"
    "Answer:"
)
query_engine = index.as_query_engine(
    similarity_top_k=10,
     text_qa_template=qa_prompt
     )