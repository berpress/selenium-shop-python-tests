from fixtures.constants import RegisterConstants, AuthConstants
from fixtures.models.register import RegisterData


class TestLoginPage:
    def test_login_exist_user(self, app):
        """
        Steps:
        1. Open main page
        2. Register new user with valid data
        3. Login with data from step 2
        """
        app.open_main_page()
        data = RegisterData.random()
        app.register.register(data=data)
        assert app.register.get_toast_text() == RegisterConstants.SUCCESS
        app.login.auth(data)
        assert app.login.get_toast_text() == RegisterConstants.SUCCESS

    def test_none_exist_user(self, app):
        """
        Steps:
        1. Open main page
        2. Login with random data
        3. Check error
        """
        app.open_main_page()
        data = RegisterData.random()
        app.login.auth(data=data)
        assert app.login.get_toast_text() == AuthConstants.INVALID_CRED
