import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings,PromptTemplate
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# 1. LOAD API KEY
# Make sure you have a .env file with OPENAI_API_KEY=sk-...
load_dotenv()

# 2. CONFIGURE SETTINGS FOR OPENAI
# This offloads all heavy math and logic to the cloud
print("☁️ Connecting to OpenAI...")

# Standard high-performance model for 2026
Settings.llm = OpenAI(model="gpt-4o", 
            temperature=0.3,
system_prompt=(
        "You are a strict Islamic History assistant created by Wali Mohamed "
        "I am an expert in transliteration. I understand that names can be spelled differently "
    "(e.g., Umar/Omar, Uthman/Osman, Muhammad/Mohammed). "
    "When a user asks about a person, I will look for all common spelling variations "
    "within the provided context to find the answer."
        "Your ONLY source of truth is the provided context. "
        "If the answer is not in the context, say 'I am sorry, but the provided "
        "documents do not contain information about this.' "
        "Do not use outside knowledge."
    )
    )

# High-quality embeddings (replaces BAAI local model)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# 3. LOAD DATA
print("📚 Loading your Wikipedia articles...")
if not os.path.exists("./history_pages"):
    print("❌ Error: './history_pages' folder not found!")
else:
    reader = SimpleDirectoryReader("./history_pages")
    documents = reader.load_data()

    # 4. BUILD INDEX
    # Note: This will now use OpenAI credits to 'embed' your documents
    print("🧠 Building the AI brain in the cloud... please wait.")
    index = VectorStoreIndex.from_documents(documents)
    qa_prompt_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Instruction: If the user greets you (e.g., 'Hi', 'Salam'), respond politely "
    "For factual questions,Using ONLY the context above, answer: {query_str}\n"
    "If the answer isn't there, say you don't know based on these documents."
    )
    qa_prompt = PromptTemplate(qa_prompt_str)
    # 5. CREATE QUERY ENGINE
    query_engine = index.as_query_engine(streaming=True,
      # 'refine' or 'compact' ensures it sticks to the text found
            response_mode="compact",
            text_qa_template=qa_prompt,
    similarity_top_k=5  # Increase this from the default 2 or 3
    )

   
    # 6. CHAT LOOP
    # This prints the intro once as soon as the project is ready
    print("\n" + "="*30)
    print(" Assalamu Alaikum! I am your Islamic History Assistant.")
    print(" Created by Wali Mohamed.")
    print("="*30)
    print("\n✅ Project Ready! Ask me about Islamic History.")
    print("(Type 'exit' to quit)\n")

    while True:
        text_input = input("User: ")
        if text_input.lower() == "exit":
            break
        
        response = query_engine.query(text_input)
        print("\nAI Assistant: ", end="")
        response.print_response_stream()
        print("\n")