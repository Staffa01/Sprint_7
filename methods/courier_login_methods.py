from .base_requests import BaseRequest
from common.endpoints import *
from common.helpers import *
import allure

class CourierLoginMethods(BaseRequest):
    @allure.step(f'Запрос на авторизацию {Courier.LOGIN}')
    def login(self, not_send=None, replace_param=None):
        payload = generate_not_valid_courier_payload(not_send, replace_param)
        resp = self.post_request(BASE_URL, Courier.LOGIN, data=payload)
        return resp