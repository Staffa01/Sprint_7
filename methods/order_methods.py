from .base_requests import BaseRequest
from common.endpoints import *
from common.data import *
import allure


class OrderMethods(BaseRequest):
    @allure.step(f'Запрос на создание заказа {Order.BASE}')
    def create(self, color):
        payload = generate_order_payload(color)
        resp = self.post_request(BASE_URL,Order.BASE,data=payload)
        return resp
    
    @allure.step(f'Запрос на получение списка заказов {Order.BASE}')
    def get_list_orders(self):
        resp = self.get_request(BASE_URL, Order.BASE)
        return resp