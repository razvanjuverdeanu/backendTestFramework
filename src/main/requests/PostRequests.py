import requests

from src.main.endpoints.Endpoints import *


def createStudentRequest(jsonData):
    resp = requests.post(BASE_URL, json=jsonData)
    return resp
