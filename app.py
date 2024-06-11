import streamlit as st

st.title('Football Team')

player_info = {
    'age': st.number_input('Age'),
    'height': st.number_input('Height(cm)'),
    'weight': st.number_input('Weight(kg)'),
}

st.button('Run')

st.write(f'Player: {player_info["age"]}')