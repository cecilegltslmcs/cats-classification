#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import pandas as pd
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.frontend import get_predictions, main


class TestFrontend(unittest.TestCase):
    @patch("requests.post")
    @patch("streamlit.file_uploader")
    @patch("streamlit.image")
    def test_get_predictions(self, mock_image, mock_file_uploader, mock_requests_post):
        """
        Test the get_predictions function.

        This test case checks the behavior of the get_predictions function
        when provided with mock image data. It ensures that the function returns
        a DataFrame with the expected structure and that the percentages sum up
        to 100.
        """

        mock_file_uploader.return_value = MagicMock()
        mock_file_uploader.return_value.getvalue.return_value = b"mock_image_data"
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Ragdoll": 0.80,
            "Bombay": 0.15,
            "American Curl": 0.05,
            "Birman": 0,
            "Egyptian Mau": 0,
            "Bengal": 0,
            "Siamese": 0,
            "Maine Coon": 0,
            "American Bobtail": 0,
            "Turkish Angora": 0,
            "Russian Blue": 0,
            "British Shorthair": 0,
            "Persian": 0,
            "Abyssinian": 0,
            "Norwegian Forest": 0,
            "Manx": 0,
            "Scottish Fold": 0,
            "American Shorthair": 0,
            "Exotic Shorthair": 0,
            "Sphynx": 0,
        }
        mock_requests_post.return_value = mock_response

        predictions = get_predictions(mock_file_uploader.return_value.getvalue())

        self.assertIsInstance(predictions, pd.DataFrame)
        self.assertEqual(len(predictions), 20)
        self.assertEqual(predictions.columns.tolist(), ["Breed", "Percentage"])
        self.assertEqual(sum(predictions["Percentage"]), 100.0)

        # Breed names and percentages assertion
        expected_breeds = ["Ragdoll", "Bombay", "American Curl"]
        expected_percentages = [80, 15, 5]
        for breed, percentage in zip(expected_breeds, expected_percentages):
            self.assertIn(breed, predictions["Breed"].tolist())
            self.assertAlmostEqual(
                predictions.loc[predictions["Breed"] == breed, "Percentage"].values[0],
                percentage,
                places=5,
            )

    @patch("requests.post")
    @patch("streamlit.file_uploader")
    def test_get_predictions_exception_handling(
        self, mock_file_uploader, mock_requests_post
    ):
        """
        Test the error handling in the get_predictions function.

        This test case checks how the get_predictions function handles an exception
        when the requests.post call raises a requests.RequestException. It ensures
        that the function gracefully handles the error scenario and returns None.
        """

        mock_file_uploader.return_value = MagicMock()
        mock_file_uploader.return_value.getvalue.return_value = b"mock_image_data"

        with patch(
            "requests.post", side_effect=requests.RequestException("Mocked exception")
        ):
            predictions = get_predictions(mock_file_uploader.return_value.getvalue())

        self.assertIsNone(predictions)


if __name__ == "__main__":
    unittest.main()
