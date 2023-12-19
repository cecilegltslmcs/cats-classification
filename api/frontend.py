# import libraries
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import os

host = os.getenv("BACKEND_URL", "http://localhost:8000/predict")

# Displaying in head
st.title("Cat Breeds Classifier")
st.image("https://cdn.pixabay.com/photo/2023/12/08/23/46/cat-8438334_960_720.jpg")
st.text("Upload a cat picture to obtain its breed. Only 20 breeds available.")

# Displaying uploader
uploaded_file = st.file_uploader("Upload your image...", type="jpg")


if uploaded_file is not None:
    st.image(uploaded_file.getvalue())
    file = {"file": uploaded_file.getvalue()}
    res = requests.post(host, timeout=20, files=file)
    res_path = res.json()
    sorted_answer = sorted(res_path.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_answer, index=[0])
    answer_df = pd.DataFrame.from_dict(converted_dict, orient="index")
    answer_df.reset_index(inplace=True)
    answer_df.rename(columns={0: "Percentage", "index": "Breed"}, inplace=True)
    answer_df.drop(index=answer_df.index[-1], axis=0, inplace=True)
    answer_df["Percentage"] = answer_df["Percentage"] * 100
    st.subheader("🐱 Purr! I'm a :")
    fig = px.pie(answer_df.head(3), names="Breed", labels="Breed", values="Percentage")
    fig.update_traces(hoverinfo="label+percent", textinfo="label+value")

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(answer_df)
