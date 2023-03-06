import streamlit as st
import base64



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
    
    st.markdown("""
    <style>
        .glass-card {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 100%;
            background-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) inset, 0 0 20px rgba(0, 0, 0, 0.2);
            border-radius: 20px;
            padding: 5%;
          
        }

         .column card {
            flex-basis: 35%;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 5%;
            filter: blur(10px);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="width:100%">
       <div class="column">Column 1</div>
       <div class="column">Column 2</div>
    </div>
    """, unsafe_allow_html=True)
add_bg_from_local('image.jpg')    


