from faker import Faker

fake = Faker()


class RegisterData:
    def __init__(self, email: str = None, password: str = None, password_2: str = None):
        self.email = email
        self.password = password
        self.password_2 = password_2

    @staticmethod
    def random():
        email = fake.email()
        password = fake.password()
        password_2 = password
        return RegisterData(email=email, password=password, password_2=password_2)
