# NEXUS AI – AI Chatbot with LangChain Memory

## Project Description

NEXUS AI is an intelligent AI-powered chatbot application developed using Python, Streamlit, LangChain, and Groq API. It allows users to interact with an AI assistant, receive intelligent responses, and maintain conversation history using LangChain memory.

## Live Demo

https://local-memory-chatbot-euloz5vhphfszsbhyzjrxe.streamlit.app/

## Features

- AI-powered chatbot
- Interactive user interface
- Conversation memory using LangChain
- Context-aware responses
- Chat history management
- Clear conversation option
- Fast AI response generation
- Cloud deployment support

## Technologies Used

- Python
- Streamlit
- LangChain
- LangChain Core
- LangChain Groq
- Groq API
- Llama 3.3 70B Versatile

## Project Structure

    Local-Memory-Chatbot/
    ├── app.py
    ├── requirements.txt
    └── README.md

## Installation

### Step 1: Clone Repository

    git clone https://github.com/thansii1607-ops/Local-Memory-Chatbot.git

### Step 2: Open Project Folder

    cd Local-Memory-Chatbot

### Step 3: Install Dependencies

    pip install -r requirements.txt

### Step 4: Configure API Key

Create a .streamlit/secrets.toml file and add:

    GROQ_API_KEY = "your_groq_api_key"

### Step 5: Run Application

    python -m streamlit run app.py

## Working Process

1. User enters a message in the chatbot.
2. LangChain processes the conversation.
3. Conversation memory maintains previous messages.
4. Groq API sends the request to the AI model.
5. The AI model generates a response.
6. The chatbot displays the response.

## LangChain Memory

The application uses InMemoryChatMessageHistory and RunnableWithMessageHistory to maintain conversation history during the active session.

This helps the chatbot understand previous messages and provide context-aware responses.

## Future Enhancements

- User authentication
- Multiple chat sessions
- Permanent chat history
- Voice interaction
- File upload support

## Conclusion

NEXUS AI demonstrates the integration of Large Language Models, LangChain, and conversation memory to build an interactive AI chatbot application.

