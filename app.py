import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from PIL import Image
import base64


# from llm import chat
from gemini import chat
st.set_page_config(page_title="IDHAR - Football Team",
                   page_icon="🦾",
                   layout="wide",
                   initial_sidebar_state="collapsed")
st.title('Football Team')
ICON_IMAGE = "data/logo.png"
st.logo(ICON_IMAGE)
st.sidebar.markdown("Hi! I'm idhar! What's your question!")

# prompt = st.sidebar.chat_input("Say sth")

# if prompt:
#     st.sidebar.write(f"User said: {prompt}")
with st.sidebar:
    messages = st.container()
    if prompt := st.chat_input("Say something"):
        anwser = chat(prompt)
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(anwser)
 
# player_info = {
#     'age': st.number_input('Age'),
#     'height': st.number_input('Height(cm)'),
#     'weight': st.number_input('Weight(kg)'),
# }

# st.button('Run')

# st.write(f'Player: {player_info["age"]}')

# Transfer image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode("utf-8")
    return b64_string



nodes = []
edges = []
b64_pic = []
zzc_b64 = image_to_base64("data/zzc.png")
lcm_b64 = image_to_base64("data/lcm.png")
cyq_b64 = image_to_base64("data/cyq.png")
ldj_b64 = image_to_base64("data/ldj.png")
ljw_b64 = image_to_base64("data/ljw.png")
lzx_b64 = image_to_base64("data/lzx.png")

nodes.append( Node(id="zzc", 
                   label="CF",
                   size=80, 
                   shape="circularImage",
                   image=f"data:image/png;base64,{zzc_b64}") 
            ) # includes **kwargs
nodes.append( Node(id="lcm", 
                   label="slave",
                   size=50, 
                   shape="circularImage",
                   image=f"data:image/png;base64,{lcm_b64}")
            )
nodes.append( Node(id="cyq",
                   label="yangkun",
                   size=50, 
                   shape="circularImage",
                   image=f"data:image/png;base64,{cyq_b64}")
            )
nodes.append( Node(id="ldj",
                   label="CB",
                   size=50, 
                   shape="circularImage",
                   image=f"data:image/png;base64,{ldj_b64}")
            )
nodes.append( Node(id="ljw",
                   label="lagabu",
                   size=50, 
                   shape="circularImage",
                   image=f"data:image/png;base64,{ljw_b64}")
            )
nodes.append( Node(id="lzx",
                   label="runner",
                   size=50, 
                   shape="circularImage",
                   image=f"data:image/png;base64,{lzx_b64}")
            )
edges.append( Edge(source="lcm", 
                   label="idhar's son", 
                   target="zzc", 
                   length=300
                   # **kwargs
                   ) 
            ) 
edges.append( Edge(source="ldj", 
                   label="teammate", 
                   target="zzc", 
                   length=300
                   # **kwargs
                   ) 
            ) 
edges.append( Edge(source="cyq", 
                   label="teammate", 
                   target="zzc", 
                   length=300
                   # **kwargs
                   ) 
            ) 
edges.append( Edge(source="ljw", 
                   label="idhar's pet", 
                   target="zzc", 
                   length=300
                   # **kwargs
                   ) 
            ) 
edges.append( Edge(source="lzx", 
                   label="teammate", 
                   target="zzc", 
                   length=300
                   # **kwargs
                   ) 
            ) 

config = Config(width=1000,
                height=1000,
                directed=False, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)