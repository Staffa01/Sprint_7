import allure
import pytest
from methods.courier_register_metods import CourierRegisterMethods
from common.helpers import *


class TestCourierRegistration:
    courier = CourierRegisterMethods()

    @allure.title(f'Тест создания курьера')
    def test_courier_create(self):
        resp = self.courier.create()
        status = 201
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()['ok'], f'Курьер не создан {resp.json()}'

    @allure.title(f'Тест создания курьера с уже существующим логином')
    def test_courier_create_already_exists(self):
        resp = self.courier.create_already_exists()
        status = 409
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()['message'] == 'Этот логин уже используется. Попробуйте другой.', f'Дубликат курьера создан {resp.json()}'

    @allure.title(f'Тест создания курьера без обязательного параметра в запросе')
    @pytest.mark.parametrize('not_create', ['login','password'])
    def test_courier_create_with_not_walid_payload(self, not_create):
        resp = self.courier.create(not_create)
        status = 400
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()['message'] == 'Недостаточно данных для создания учетной записи', f'Курьер не создан {resp.json()}'
    

