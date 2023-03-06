
import base64
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from streamlit_card import card
st.set_page_config(page_title="My App", page_icon=":rocket:", layout="centered",initial_sidebar_state="expanded"  )

# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

navbar = option_menu("Output", [""],
                         icons=['cpu', 'lightbulb fill', 'bar-chart fill', 'book','person dash'],
                         menu_icon="menu-button", default_index=0, orientation='horizontal',
                         styles={
        "container": {"background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1);","backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3);"},
        "icon": {"font-color":"Grey", "font-size": "25px", "border-radius":"50%"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    }
    )



with st.sidebar:
    choose = option_menu("App Gallery", ["Write For Me", "Idea Generator", "Promotion Ideas", "Account", "Log Out"],
                         icons=['cpu', 'lightbulb fill', 'bar-chart fill', 'book','person dash'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important","background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)","backdrop-filter": "blur(5px)","-webkit-backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3)"},
        "icon": {"font-color":"Grey", "font-size": "25px", "border-radius":"50%"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    }
    )

    with st.container():
        box=option_menu("Trial Pack", ["Click to subscribe"],
                         icons=['currency-exchange'],
                         menu_icon="activity", default_index=0,
                        styles={
        "container": {"padding": "5!important","background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)","backdrop-filter": "blur(5px)","-webkit-backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3)"},
        "icon": {"font-color":"Grey", "font-size": "25px", "border-radius":"50%"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
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
        background-size: cover;
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