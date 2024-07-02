import pytest

from src.main.models.OkResponse import *
from src.main.requests.GetRequests import *


@pytest.mark.order(2)
def test_all_students():
    response = getAllStudRequest()
    assert (response.status_code == 200)
    response_json = response.json()
    assert (len(response_json) > 0)
    for stud in response_json:
        print(stud)


@pytest.mark.order(1)
def test_get_stud_by_id():
    response = getStudRequestById("1").json()
    try:
        obj = OkResponse(**response)
        assert (obj is not None)
        print(obj)
    except:
        raise Exception(response['message'])
