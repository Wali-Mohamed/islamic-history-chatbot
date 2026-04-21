import streamlit as st
from rag import query_engine

st.set_page_config(page_title="Islamic History Assistant", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #000000; color: #ffffff; }
div[data-testid="stChatMessage"] { background-color: #111111; padding: 12px; border-radius: 10px; }
div[data-testid="stChatMessage"] * { color: #ffffff !important; }
div[data-testid="stChatInput"] textarea { background-color: #111111; color: #ffffff; }
</style>
""", unsafe_allow_html=True)

st.title("Islamic History Assistant")
st.markdown(
    "<p style='color:gray; font-size:14px;'>Created by Wali Mohamed</p>",
    unsafe_allow_html=True
)

if "history" not in st.session_state:
    st.session_state.history = []

# DISPLAY CHAT
for role, msg in st.session_state.history:
    st.write(f"**{role}:** {msg}")

# INPUT (THIS is the correct way)
user_input = st.chat_input("Ask a question")

if user_input:
    response = query_engine.query(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("AI", str(response)))

    st.rerun()