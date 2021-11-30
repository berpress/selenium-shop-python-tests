import pytest
from fixtures.constants import RegisterConstants
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
        assert app.register.get_toast_text() == RegisterConstants.SUCCESS

    @pytest.mark.parametrize("field", ["password", "password_2"])
    def test_register_user_empty_password(self, app, field):
        """
        Steps:
        1. Open main page
        2. Register new user with empty password
        """
        app.open_main_page()
        data = RegisterData.random()
        setattr(data, field, None)
        app.register.register(data=data)
        assert app.register.get_error() == RegisterConstants.ERROR_PASSWORD
