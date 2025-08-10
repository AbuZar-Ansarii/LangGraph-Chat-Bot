# 🤖 ECHO ChatBot — LangGraph + Streamlit + SQLite

A conversational AI chatbot built with **LangGraph**, **LangChain**, and **Streamlit**, powered by **Google Generative AI** (Gemini).  
Chats are stored **persistently** in a local **SQLite** database, so you can revisit old conversations anytime.
---
## 🚀 Features

- 💬 **Multi-threaded conversations** (each chat session stored separately)
- 🗂 **Sidebar with chat list** showing the **first user message** instead of an ugly UUID
- 💾 **SQLite persistence** to store all messages
- 📜 Conversation history is **loaded** when you switch threads
- ⚡ **Streaming responses** from Gemini for real-time AI typing effect
- 🔄 "New Chat" button to start fresh threads
- 🛠 Easily extendable with other LLM providers
---

## Sample Images
<img width="1920" height="1080" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/c81fe2f9-4242-451b-b388-21af1347c893" />
<img width="1920" height="1080" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/b17288f2-0a31-4402-9218-d724d05e9b4b" />
<img width="1920" height="1080" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/68fae6c4-38e3-4c2b-beb9-38f8e4a2b0af" />
<img width="1920" height="1080" alt="Screenshot (68)" src="https://github.com/user-attachments/assets/041c64e0-65ac-4d44-8c83-00bc8f10dc45" />
<img width="1920" height="1080" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/7676e293-c5bc-438b-8e7a-7809e55be969" />
<img width="1920" height="1080" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/5d925e4a-001e-45cb-b4cd-6709ed2a2adf" />
<img width="1920" height="1080" alt="Screenshot (71)" src="https://github.com/user-attachments/assets/cc3a24e6-370e-422e-acba-e183fd311e7c" />
<img width="1920" height="1080" alt="Screenshot (73)" src="https://github.com/user-attachments/assets/6f12fb51-2976-4056-9e07-f78cb03bc93c" />


---
## 🛠 Setup

### 1️⃣ Clone the repo

```bash
git clone https://github.com/AbuZar-Ansarii/LangGraph-Chat-Bot.git
cd echo-chatbot

