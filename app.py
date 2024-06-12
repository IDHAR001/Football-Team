import streamlit as st
# from llm import chat
from gemini import chat
st.set_page_config(page_title="IDHAR - Football Team",
                   page_icon="🦾",
                   layout="wide",
                   initial_sidebar_state="collapsed")
st.title('Football Team')
ICON_IMAGE = "data/logo.png"
st.logo(ICON_IMAGE)
st.sidebar.markdown("Hi! I'm idhar!")

# prompt = st.sidebar.chat_input("Say sth")

# if prompt:
#     st.sidebar.write(f"User said: {prompt}")
with st.sidebar:
    messages = st.container()
    if prompt := st.chat_input("Say something"):
        anwser = chat(prompt)
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(anwser)
 
player_info = {
    'age': st.number_input('Age'),
    'height': st.number_input('Height(cm)'),
    'weight': st.number_input('Weight(kg)'),
}

st.button('Run')

st.write(f'Player: {player_info["age"]}')