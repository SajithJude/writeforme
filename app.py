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
            background-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) inset, 0 0 20px rgba(0, 0, 0, 0.2);
            border-radius: 20px;
            padding: 20px;
            width: 90%
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h1>Transparent Glassmorphic Streamlit Card</h1>
        <p>This is an example of a transparent Glassmorphic Streamlit card.</p>
    </div>
    """, unsafe_allow_html=True)
add_bg_from_local('image.jpg')    


    