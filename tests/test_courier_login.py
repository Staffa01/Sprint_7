import allure
import pytest
from methods.courier_login_methods import CourierLoginMethods
from common.helpers import *
from common.data import *


class TestCourierLogin:
    courier = CourierLoginMethods()
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