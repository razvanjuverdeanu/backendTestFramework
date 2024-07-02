from dataclasses import dataclass


@dataclass
class OkResponse:
    name: str
    surname: str
    city: str
    profile: str
    email: str
    dateOfBirth: str
    id: int
    age: int
