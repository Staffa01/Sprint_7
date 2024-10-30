from .base_requests import BaseRequest
from common.endpoints import *
from common.data import *
import allure

class CourierMethods(BaseRequest):
    @allure.step(f'Запрос на регистрацию {Courier.BASE}')
    def create(self, not_send = None):
        payload = generate_register_payload(10)
        if not_send != None:
            del payload[not_send]
        resp = self.post_request(BASE_URL,Courier.BASE,data=payload)
        return resp


    @allure.step(f'Запрос на регистрацию уже существующего пользователя {Courier.BASE}')
    def create_already_exists(self):
        resp = self.post_request(BASE_URL,Courier.BASE,data=AUTORISED_USER_PAYLOAD)
        return resp
    
    @allure.step(f'Запрос на авторизацию {Courier.LOGIN}')
    def login(self, not_send = None, replace_param = None):
        payload = generate_not_valid_courier_payload(not_send, replace_param)
        print(payload)
        resp = self.post_request(BASE_URL, Courier.LOGIN, data=payload)
        return resp
    
