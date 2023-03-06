import streamlit as st


st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(to bottom right, #00ffff, #ff00ff);
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.write("Hello world")


# Define the CSS style
slider_style = """
<style>
    .css-1tj0q0g-ValueContainer {
        font-size: 24px !important;
    }
</style>
"""

# Render the slider component
st.markdown(slider_style, unsafe_allow_html=True)
slider_val = st.slider("Select a value", 0, 10, 5)
# Add your Streamlit app code here
