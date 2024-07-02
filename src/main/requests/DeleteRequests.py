import requests

from src.main.endpoints.Endpoints import *


def deleteAllStudentRequest():
    resp = requests.delete(BASE_URL + ALL)
    return resp


def deleteStududentRequestById(id):
    resp = requests.delete(BASE_URL + str(id))
    return resp
