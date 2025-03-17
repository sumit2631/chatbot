import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
# Streamlit UI: Title for the application
st.title("LLM Chatbot")

# File uploader widget for accepting PDF documents
st.sidebar.title("Key Information")
st.sidebar.text("Please enter the information\nto start the application.")
groq_id=st.sidebar.text_input("Enter your Groq API Key",type='password')
if groq_id:
    try:
        # Define the prompt for the ChatGroq language model
        prompt=ChatPromptTemplate.from_template(
            """ You are a helpfull AI assistant. try to answer the user questions.
            Question:{input}"""
            )
        # Initialize the ChatGroq language model
        llm=ChatGroq(model='Gemma2-9b-it',groq_api_key=str(groq_id))
        # Create a document processing chain with the LLM and custom prompt
        chain=prompt|llm|parser
        # Input widget for user queries
        user=st.text_input("What's your question?")
        if user:
            answer=chain.invoke({'input':user})
            st.write(answer)
    except:
        st.error("Please enter the API key correctly")