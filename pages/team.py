import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import base64

st.set_page_config(page_title="Football Team", layout="wide")

st.title('Football Team')

# Transfer image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode("utf-8")
    return b64_string

nodes = []
edges = []
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



