import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EAACwrNebricBAGLtTpt1yhR7y3DW9LHZBEjWZAShNS6Lgv17CkaWatb3iWJe6rmyr6aZCZB3prZCShKtYUIwg4IMvhOfYgw1HoE0N7ZCZC6qtzsiUdGghN9MJWZC7Q2or4CLJOBsRrObxnhZCOZCqB9qMZC5UM49B3kyy9h4AyDDfpz0gZDZD")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
