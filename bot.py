import streamlit as st
import json
from app.services import getMoviesByPront
from app.redis import get_redis
from app.config.settings import api_settings

EX_CACHE = 60

# Inicializar Redis
redis = get_redis()


def run():
    st.set_page_config(
        page_title=api_settings.TITLE,
        page_icon="✅",
        layout="wide",
        # initial_sidebar_state="expanded",
    )

    # Cargar el historial de mensajes desde Redis al inicio de la aplicación
    if "messages" not in st.session_state:
        # Intentar cargar desde Redis
        stored_messages = redis.get("chat_history")
        if stored_messages:
            st.session_state.messages = json.loads(stored_messages)
        else:
            st.session_state.messages = []

    n_results = st.sidebar.selectbox("Select number of results", [1, 2, 3, 4, 5], index=1)
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
        # n_results = 2
        response = getMoviesByPront(prompt,n_results)

        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        redis.set("chat_history", json.dumps(st.session_state.messages))

if __name__ == '__main__':
    run()