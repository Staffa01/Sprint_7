import allure
import pytest
from common.data import *
from methods.order_methods import OrderMethods

class TestOrder:
    order = OrderMethods()

    @allure.title("Проверка успешного оформления заказа")
    @pytest.mark.parametrize('color', ([["BLACK"], ["GRAY"],["BLACK","GREY"],[""]]))
    def test_order_create(self, color):
        resp = self.order.create(color)
        status = 201
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()["track"] != None, "Заказ не оформлен"

    @allure.title("Проверка получения списка заказов")
    def test_order_get(self):
        resp = self.order.get_list_orders()
        status = 200
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()["orders"] != None, "Список заказов не получен"
       