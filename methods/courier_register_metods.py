from .base_requests import BaseRequest
from common.endpoints import *
from common.data import *
from common.helpers import *
import allure

class CourierRegisterMethods(BaseRequest):
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
    

    
