from .base_requests import BaseRequest
from common.endpoints import *
from common.data import *
import allure

class CourierMethods(BaseRequest):
    @allure.step(f'Запрос на регистрацию {Courier.BASE}')
    def create(self):
        payload = generate_register_payload(10)
        resp = self.post_request(BASE_URL,Courier.BASE,data=payload)
        return resp