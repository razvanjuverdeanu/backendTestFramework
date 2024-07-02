import pytest

from src.main.requests.DeleteRequests import *


@pytest.mark.order(2)
def test_delete_all_students():
    response = deleteAllStudentRequest()
    assert (response.status_code == 202)
    print(response.text.__eq__("All students were deleted"))


@pytest.mark.order(1)
def test_delete_student_by_id():
    id = 5
    response = deleteStududentRequestById(id)
    assert (response.status_code == 202)
    assert (response.text.__eq__("Student with id " + str(id) + " was deleted"))
