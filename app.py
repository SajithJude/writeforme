
import base64
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from streamlit_card import card


st.set_page_config(page_title="My App", page_icon=":rocket:", layout="wide", )



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
    

if choose == "Write For Me":
    st.markdown(""" <style> .columns_in_form2 {
    font-size:16px ; color:"#fafafa"; border-radius:10px;} 
    </style> """, unsafe_allow_html=True)
    # st.markdown('<p class="font">Write For Me</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        des=st.text_input(label='Description') #Collect user feedback
        para=st.text_input(label='Parameter') #Collect user feedback
        # Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Submitted!')
