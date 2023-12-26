#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Frontend Module

This module contains functions related to the fetching and the displaying of the
predictions.
"""

# import libraries
import os
from typing import Union
import pandas as pd
import plotly.express as px
import requests
import streamlit as st


def get_predictions(image_file: Union[bytes, memoryview]) -> pd.DataFrame:
    """
    Takes an images and return a DataFrame with predictions.

    Parameters
    ----------
    image_file Union[bytes, memoryview]:
        Image given by the user.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing breeds with related percentage.
    """
    backend_url = os.getenv("BACKEND_URL", "http://localhost:8000/predict")
    file = {"file": image_file}

    try:
        response = requests.post(
            f"http://{backend_url}/predict", timeout=20, files=file
        )
        response.raise_for_status()

        predictions = response.json()
        sorted_predictions = sorted(
            predictions.items(), key=lambda x: x[1], reverse=True
        )
        converted_dict = dict(sorted_predictions, index=[0])
        answer_df = pd.DataFrame.from_dict(converted_dict, orient="index")
        answer_df.reset_index(inplace=True)
        answer_df.rename(columns={0: "Percentage", "index": "Breed"}, inplace=True)
        answer_df.drop(index=answer_df.index[-1], axis=0, inplace=True)
        answer_df["Percentage"] = answer_df["Percentage"] * 100
        return answer_df

    except requests.RequestException as e:
        st.error(f"Error: {str(e)}")
        return None


def main():
    """
    Main function for the Cats Breeds Classifier application.

    This function sets up the Streamlit user interface
    for uploading a cat image, fetching predictions
    using the backend API, and displaying the results.

    Usage:
    1. Run this script.
    2. Visit the provided Streamlit URL in your web browser.
    3. Upload a cat picture to obtain its predicted breed.

    The application displays the top three predicted breeds along with their
    corresponding percentages in a pie chart and a tabular format.

    """
    st.title("Cats Breeds Classifier")
    st.image(
        """https://cdn.pixabay.com/photo/
    2023/12/08/23/46/cat-8438334_960_720.jpg"""
    )
    st.text(
        """Upload a cat picture to obtain its breed.
    Only 20 breeds available."""
    )

    uploaded_file = st.file_uploader("Upload your image...", type="jpg")

    if uploaded_file is not None:
        st.image(uploaded_file.getvalue())

        predictions = get_predictions(uploaded_file.getvalue())

        if predictions is not None:
            st.subheader("🐱 Purr! I'm a :")
            fig = px.pie(
                predictions.head(3), names="Breed", labels="Breed", values="Percentage"
            )
            fig.update_traces(hoverinfo="label+percent", textinfo="label+value")

            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(predictions)


if __name__ == "__main__":
    main()
