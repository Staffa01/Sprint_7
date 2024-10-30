import allure
import pytest
from methods.courier_metods import CourierMethods
from common.data import *


class TestCourier:
    courier = CourierMethods()

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
    
    @allure.title(f'Тест авторизации курьера')
    def test_courier_login(self):
        resp = self.courier.login()
        status = 200
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()['id'] == AUTORISED_USER_ID, f'Курьер не авторизован {resp.json()}'

    @allure.title(f'Тест авторизации курьера без обязательного параметра')
    @pytest.mark.parametrize('not_send', ['login','password'])
    def test_courier_login_not_send_required_param(self, not_send):
        resp = self.courier.login(not_send = not_send)
        status = 400
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()['message'] == 'Недостаточно данных для входа', f'Курьер авторизован {resp.json()}'

    @allure.title(f'Тест авторизации курьера с невалидными данными')
    @pytest.mark.parametrize('replace_param', ['login','password'])
    def test_courier_login_with_send_not_walid_param(self, replace_param):
        resp = self.courier.login(replace_param = replace_param)
        status = 404
        assert resp.status_code == status, assert_message(status, resp.status_code, resp.json())
        assert resp.json()['message'] == 'Учетная запись не найдена', f'Курьер авторизован {resp.json()}'
