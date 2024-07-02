import requests

from src.main.endpoints.Endpoints import *


def getAllStudRequest():
    resp = requests.get(BASE_URL + ALL)
    return resp


def getStudRequestById(id):
    resp = requests.get(BASE_URL + str(id))
    return resp
