import streamlit as st
from llm import load_llm
from chat import load_chat

st.set_page_config(page_title="Home Page",
                   page_icon="🦾",
                   layout="wide",
                   initial_sidebar_state="collapsed")

st.title('Home Page')

ICON_IMAGE = "data/logo.png"
st.logo(ICON_IMAGE)
st.sidebar.markdown("Hi! I'm idhar! What's your question!")

# select llm
llm_selectbox = st.sidebar.selectbox(
    "Select your LLM",
    ("Gemini", "Kimi")
)

loaded_llm = load_llm(llm_selectbox)


with st.sidebar:
    messages = st.container()
    if prompt := st.chat_input("Say something"):
        anwser = load_chat(loaded_llm, prompt)
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(anwser)

with st.container():
    st.header("Player Info")
    player_info = {
        'age': st.number_input('Age', min_value=1, max_value=60),
        'height': st.number_input('Height(cm)'),
        'weight': st.number_input('Weight(kg)'),
        }

    run = st.button('Run')
    if run:
        st.write(f'Player age: {player_info["age"]}')


