import streamlit as st
from back_bot import chat_bot, get_all_threads
import uuid
from langchain_core.messages import HumanMessage

# ******************* UTILITY FUNCTIONS ********************************

def create_thread_id():
    return str(uuid.uuid4())

def reset_chat():
    thread_id = create_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chat_bot.get_state(config={'configurable': {"thread_id": thread_id}}).values
    return state.get('messages', [])  

def get_thread_title(thread_id):
    """Return the first message content as thread title, fallback to thread_id."""
    messages = load_conversation(thread_id)
    if messages:
        return messages[0].content[:30] + ("..." if len(messages[0].content) > 30 else "")
    return f"Chat {thread_id[:12]}"

# ************************ ESSENTIAL STUFF *****************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = create_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state['chat_threads'] = get_all_threads()

add_thread(st.session_state['thread_id'])

CONFIG = {'configurable': {"thread_id": st.session_state['thread_id']}}

# ************************* SIDEBAR ************************************

st.sidebar.title("🦅FALCON")

if st.sidebar.button("💬New Chat"):
    reset_chat()

st.sidebar.header("Recent Chats")

for thread_id in st.session_state['chat_threads'][::-1]:
    thread_title = get_thread_title(thread_id)
    if st.sidebar.button(thread_title, key=f"btn_{thread_id}"):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []
        for msg in messages:
            role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages

# ************************ MAIN SCREEN **********************************



# Display chat history before input
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

user_input = st.chat_input("Ask Me Anything...")



if not user_input:
    st.title("🦅 HI THERE, I'M FALCON")


if user_input:
    # Store and display user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        for msg in st.session_state['message_history']:

            ai_response = st.write_stream(msg_chunk.content for msg_chunk, medadata in chat_bot.stream(
                {'messages':[HumanMessage(content=user_input)]},config=CONFIG,stream_mode='messages'
                ))
    # store ai response
    st.session_state['message_history'].append({'role':'assistant','content':ai_response})

