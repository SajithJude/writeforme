
import base64
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html


with st.sidebar:
    choose = option_menu("App Gallery", ["Write For Me", "Idea Generator", "Promotion Ideas", "Account", "Log Out"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important","margin": "5!important" ,"background-color": "#fafafa", "box-shadow": "0px 0px 20px 5px #FF69B4"},
        "icon": {"color": "white", "font-size": "25px", "background-color":"grey","border-radius":"3px","margin": "2!important"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "font-color":"Grey", "text-align": "left", "margin":"0px", "--hover-color": "#FF69B4"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #E91E63);"},
    }
    )

    with st.container():
        box=option_menu("App Gallery", ["Trial Pack"],
                         icons=['user'],
                         menu_icon="app-indicator", default_index=0,
                        styles={
        "container":{"background":"linear-gradient(to right, #9B59B6, #E91E63);","font-color":"white"},
    }
    )



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image.jpg')    
    