"""
Start tests only with started server
"""

import unittest
import requests


class TestRequestsForServer(unittest.TestCase):

    def test_posts_answers(self):
        data1 = {
            "vestibule": "west",
            "address": "West boston 45"
        }

        data2 = {
            "birthday_hum": "Jason",
            "another": "some text"
        }

        data3 = {
            "phone_number": "+7 345 235 34 67"
        }

        data4 = {
            "website_name": "google"
        }

        data5 = {
            "birthday_date": "2022-03-13",
            "address": "Bulvar rokosovskogo 45",
            "candles": 5
        }

        res1 = requests.post("http://127.0.0.1:8000/get_form/", data = data1).json()
        res2 = requests.post("http://127.0.0.1:8000/get_form/", data = data2).json()
        res3 = requests.post("http://127.0.0.1:8000/get_form/", data = data3).json()
        res4 = requests.post("http://127.0.0.1:8000/get_form/", data = data4).json()
        res5 = requests.post("http://127.0.0.1:8000/get_form/", data = data5).json()
        res6 = requests.post("http://127.0.0.1:8000/get_form/").json()

        self.assertEqual(res1, {"vestibule": "text", "address": "text"})
        self.assertEqual(res2, {"birthday_hum": "text", "another": "text"})
        self.assertEqual(res3, {'form_name': 'Store'})
        self.assertEqual(res4, {'form_name': 'Website'})
        self.assertEqual(res5, {"birthday_date": "date", "address": "text", "candles": "text"})
        self.assertEqual(res6, {"error": "request must have body"})