import allure
from methods.courier_metods import CourierMethods


class TestCourier:
    courier = CourierMethods()

    @allure.title(f'Проверка создания курьера')
    def test_courier_create(self):
        resp = self.courier.create()
        assert resp.status_code == 201, f'Ошибка метода регистрации {resp.text}'
        print(resp.json())