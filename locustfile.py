from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_list(self):
        self.client.get("/list")

    @task
    def add_record(self):
        # Her request için benzersiz, random veri
        user_name = fake.name()
        user_email = fake.unique.email()
        data = {"name": user_name, "email": user_email}
        # Eğer Flask form post’u ise Content-Type gerekebilir!
        self.client.post("/add", data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})