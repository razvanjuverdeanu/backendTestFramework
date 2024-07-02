import json

import pytest

from src.main.requests.PostRequests import *
from src.main.utils.Utils import *


@pytest.mark.order(2)
def test_create_student():
    bodyMessage = createRandomStudent()
    response = createStudentRequest(bodyMessage)
    assert (response.status_code == 201)

    # validate response method 1
    # response_json = response.json()
    # for key,value in response_json.items():
    #     bodyMessage.get(key).__eq__(value)
    #     print( key, ":", value)

    # validate response method 2
    response_json = json.loads(response.text)
    assert (response_json["name"].__eq__(bodyMessage.get("name")))
    assert (response_json["surname"].__eq__(bodyMessage.get("surname")))
    assert (response_json["city"].__eq__(bodyMessage.get("city")))
    assert (response_json["profile"].__eq__(bodyMessage.get("profile")))
    assert (response_json["email"].__eq__(bodyMessage.get("email")))
    assert (response_json["dateOfBirth"].__eq__(bodyMessage.get("dateOfBirth")))
    print(response_json)
