from fixtures.constants import BalanceConstants
from fixtures.models.balance import BalanceData


class TestBalancePage:
    def test_add_balance(self, app, login):
        """
        Steps:
        1. Login
        2. Add balance to user
        """
        data = BalanceData.random()
        app.balance.update_balance(data=data)
        assert app.register.get_toast_text() == BalanceConstants.UPDATE_BALANCE.format(
            data.money
        )
