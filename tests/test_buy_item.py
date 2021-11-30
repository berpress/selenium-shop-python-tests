from fixtures.constants import BalanceConstants, ItemsConstants
from fixtures.models.balance import BalanceData


class TestBuyPage:
    def test_buy_item(self, app, login):
        """
        Steps:
        1. Login
        2. Add balance to user
        3. Add item to cart
        4. Buy this item
        """
        data = BalanceData.random()
        app.balance.update_balance(data=data)
        assert app.register.get_toast_text() == BalanceConstants.UPDATE_BALANCE.format(
            data.money
        )
        app.items.add_to_cart()
        app.items.buy()
        assert app.items.get_toast_text() == ItemsConstants.ITEM_PAY
