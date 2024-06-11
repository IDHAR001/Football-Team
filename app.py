import streamlit as st

ICON_IMAGE = "data/logo.png"
st.logo(ICON_IMAGE)
st.sidebar.markdown("Hi!")

st.title('Football Team')

player_info = {
    'age': st.number_input('Age'),
    'height': st.number_input('Height(cm)'),
    'weight': st.number_input('Weight(kg)'),
}

st.button('Run')

st.write(f'Player: {player_info["age"]}')