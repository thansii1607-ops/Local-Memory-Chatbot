import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Nexus AI",
    page_icon="🤖",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #FFF5F7;
    color: #3D3040;
}

header {
    background-color: transparent !important;
}

.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #B65D83;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #99758A;
    font-size: 15px;
    margin-bottom: 30px;
}

[data-testid="stChatMessage"] {
    background-color: #FFFFFF;
    border: 1px solid #F0D5E1;
    border-radius: 15px;
    padding: 15px;
}

.stChatInput {
    border: 1px solid #DDA8C0;
    border-radius: 12px;
    background-color: #FFFFFF;
}

div.stButton > button {
    background-color: #B65D83;
    color: white;
    border-radius: 8px;
    border: 1px solid #B65D83;
}

div.stButton > button:hover {
    background-color: #914467;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #FCE8EF;
}

[data-testid="stSidebar"] h2 {
    color: #B65D83;
}

[data-testid="stSidebar"] p {
    color: #65475A;
}

hr {
    border-color: #F0D5E1;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_store" not in st.session_state:
    st.session_state.chat_store = {}


# ---------------- GROQ API CONFIGURATION ----------------

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

except Exception:
    st.error("Groq API Key is missing. Please configure it in Streamlit Secrets.")
    st.stop()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.7
)


# ---------------- LANGCHAIN PROMPT ----------------

prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are Nexus AI, a friendly and intelligent AI assistant.

        Your responsibilities:

        - Answer questions clearly.
        - Explain technical topics simply.
        - Help with programming and education.
        - Remember previous conversation context.
        - Give accurate and helpful responses.
        - Provide well-structured answers.
        """
    ),

    MessagesPlaceholder(variable_name="history"),

    ("human", "{input}")

])


# ---------------- CHATBOT CHAIN ----------------

chain = prompt | llm


# ---------------- MEMORY FUNCTION ----------------

def get_session_history(session_id):

    if session_id not in st.session_state.chat_store:

        st.session_state.chat_store[session_id] = (
            InMemoryChatMessageHistory()
        )

    return st.session_state.chat_store[session_id]


chatbot = RunnableWithMessageHistory(

    chain,

    get_session_history,

    input_messages_key="input",

    history_messages_key="history"

)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">NEXUS AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Intelligent AI Assistant | Powered by Groq AI'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## ⚙️ Settings")

    st.success("AI Model: Llama 3.3 70B")

    st.info("LangChain Memory: Enabled")

    st.markdown("---")

    st.markdown("### About Nexus AI")

    st.write(
        "Nexus AI is an intelligent AI chatbot "
        "built using Streamlit, LangChain and Groq."
    )

    st.markdown("---")

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.chat_store = {}

        st.rerun()


# ---------------- WELCOME SCREEN ----------------

if not st.session_state.messages:

    st.markdown("### Welcome to Nexus AI!")

    st.write(
        "Hello! I'm your AI assistant. "
        "Ask me anything about programming, "
        "technology, education or general topics."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💻 Programming Help")

    with col2:
        st.info("📚 Learn New Concepts")

    with col3:
        st.info("🧠 Intelligent Conversations")


# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------- USER INPUT ----------------

user_input = st.chat_input("Ask Nexus AI anything...")


if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Nexus AI is thinking..."):

            try:

                response = chatbot.invoke(

                    {"input": user_input},

                    config={
                        "configurable": {
                            "session_id": "nexus_user"
                        }
                    }

                )

                answer = response.content

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception:

                st.error(
                    "Unable to generate a response. "
                    "Please check your Groq API key "
                    "and try again."
                )

                st.session_state.messages.pop()
