from faker import Faker


def createRandomStudent():
    fake = Faker()
    return {"name": fake.last_name(), "surname": fake.first_name(), "city": fake.city(), "profile": fake.job(),
            "email": fake.free_email(), "dateOfBirth": fake.date_of_birth(None, 18, 99).strftime("%Y-%m-%d")}
