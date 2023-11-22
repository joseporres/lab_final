import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings



client = chromadb.PersistentClient(path="./dbmovies_default",settings=Settings(allow_reset=True))
collection = client.get_or_create_collection(name="movies")

st.title("Movies Bot")


def getMoviesByPront(prompt,n_results=1):
    results = collection.query(
    query_texts=[prompt],
    n_results=n_results
    )
    #traeme los documentos en merge por salto de linea 
    documents=  results['documents'][0]
    formated_documents = '\n'.join(documents)
    return formated_documents


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = getMoviesByPront(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

