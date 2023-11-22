import streamlit as st
import json
from app.services import getMoviesByPront, movieProntOpenAi
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

    selected_type = st.sidebar.selectbox("Select type", ["OpenAI+ChromaDB", "ChromaDB"], index=0)

    # Check if the type has changed
    if "type" not in st.session_state or st.session_state.type != selected_type:
        st.session_state.type = selected_type

        # Load chat history from Redis based on the selected type
        stored_messages = redis.get(f'{selected_type}_chat_history')
        if stored_messages:
            st.session_state.messages = json.loads(stored_messages)
        else:
            st.session_state.messages = []

    if(selected_type == "ChromaDB"):
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
        if(selected_type == "OpenAI+ChromaDB"):
            response = movieProntOpenAi(prompt)
        else:
            response = getMoviesByPront(prompt,n_results)

        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        redis.set(f'{type}_chat_history', json.dumps(st.session_state.messages))

if __name__ == '__main__':
    run()