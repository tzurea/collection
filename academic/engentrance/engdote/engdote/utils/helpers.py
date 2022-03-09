import json
import requests
from bs4 import BeautifulSoup as bs


def post_request(url, headers, data={}):
    data = json.dumps(data)
    response_data = requests.post(url, headers=headers, data=data)
    response_data = json.loads(response_data.text)
    print(response_data)
    return response_data


def get_post_data(response_data):
    session_id = response_data["examSessionId"]
    question_ids = ""
    question_list = response_data["questions"]
    for i in question_list:
        question_ids = question_ids + str(i) + ","
    question_ids = question_ids[:-1]
    post_data = {"sessionID": session_id, "questionIDs": question_ids}
    return str(question_list), post_data


def get_raw_text(data):
    data = bs(data, features="html5lib")
    data = data.get_text()
    return data
