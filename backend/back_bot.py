from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from typing import TypedDict, Annotated
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from dotenv import load_dotenv
load_dotenv()


class ChatBot_State(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

chat_llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

cnn = sqlite3.connect(database="Chat_DataBase.db",check_same_thread=False)

chekpointer = SqliteSaver(conn=cnn)

def chat_response(state: ChatBot_State):
    
    messages = state["messages"]
    
    response = chat_llm.invoke(messages)

    return{
        "messages" : [AIMessage(content=response.content)]
    }

graph = StateGraph(ChatBot_State)

graph.add_node('chat_response', chat_response)

graph.add_edge(START,'chat_response')
graph.add_edge('chat_response',END)

chat_bot = graph.compile(checkpointer=chekpointer)

def get_all_threads():
    all_threads = set()
    for check in chekpointer.list(None):
        all_threads.add(check.config['configurable']['thread_id'])
    return list(all_threads)


