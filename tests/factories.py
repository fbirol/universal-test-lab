from faker import Faker

fake = Faker()


def fake_record():
    return {"name": fake.name(), "email": fake.email()}
