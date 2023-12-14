# import libraries
import streamlit as st

# Displaying in head
st.title("Cat Breeds Classifier")
st.image("https://cdn.pixabay.com/photo/2023/12/08/23/46/cat-8438334_960_720.jpg")
st.text("Upload a cat picture to obtain its breed. Only 20 breeds available.")

# Displaying uploader
uploaded_file = st.file_uploader("Upload your image...", type="jpg")
