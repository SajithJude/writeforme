
import base64
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from streamlit_card import card


st.set_page_config(page_title="My App", page_icon=":rocket:", layout="wide",initial_sidebar_state="expanded",hide_menu=True  )



with st.sidebar:
    choose = option_menu("App Gallery", ["Write For Me", "Idea Generator", "Promotion Ideas", "Account", "Log Out"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important","margin": "1!important" ,"background-color": "#fafafa", "box-shadow": "0px 0px 20px 5px #FF69B4"},
        "icon": {"color": "white", "font-size": "25px", "border-radius":"3px","margin": "2!important"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "font-color":"Grey", "text-align": "left", "margin":"0px", "--hover-color": "#FF69B4"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #E91E63);"},
    }
    )

    with st.container():
        box=option_menu("Trial Pack", ["Click to subscribe"],
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
    
st.markdown(""" <style> 
    .form {
     border-radius:10px;
     border-width:2px;
     } 
    </style> """, unsafe_allow_html=True)

if choose == "Write For Me":
    # st.stop()
    with st.form(key="form"):
        st.subheader('Write for me')
        des=st.text_input(label='Description') 
        para=st.text_input(label='Parameter') 
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Submitted!')
            st.stop()

elif choose == "Idea Generator":
    with st.form(key="form2"):
        st.subheader('Idea Generator')
        des2=st.text_input(label='Description') 
        para2=st.text_input(label='Parameter') 
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Submitted!')
            st.stop()

elif choose == "Promotion Ideas":
    with st.form(key="form2"):
        st.subheader('Promotion Ideas')
        des2=st.text_input(label='Description') 
        para2=st.text_input(label='Parameter') 
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Submitted!')
            st.stop()