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
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-color: rgba(255, 255, 255, 0.8);
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) inset, 0 0 20px rgba(0, 0, 0, 0.2);
        padding: 20px;
    }}

    .card  {{
            display: flex;
            justify-content: center;
            align-items: center;
            background-size: cover;
            height: 300px;
            width: 500px;
        border-radius: 20px;

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

    
    
    # name = st.text_input('')

    st.markdown(f"""
    <div class="card">
      
    </div>
    """, unsafe_allow_html=True)
add_bg_from_local('image.jpg')    


