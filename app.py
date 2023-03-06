import streamlit as st
import base64

# Create a text input field and get its value
# message = f'Hello, {name}!'

# Inject the message inside a div tag
# st.markdown(f'<div style="background-color: #f0f0f0; padding: 20px;">{message}</div>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .card  {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        display: flex;
            justify-content: center;
            align-items: center;
            background-size: cover;
            background-position: center;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            color: white;
            font-size: 24px;
            text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

    


add_bg_from_local('image.jpg')    

with st.beta_container():
    st.markdown('<div class="card">Hello, world!</div>', unsafe_allow_html=True)
