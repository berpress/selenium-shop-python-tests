from fixtures.models.register import RegisterData


class TestRegisterPage:
    def test_register_new_user(self, app):
        """
        Steps:
        1. Open main page
        2. Register new user with valid data
        """
        app.open_main_page()
        data = RegisterData.random()
        app.register.register(data=data)
        pass
