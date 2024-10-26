import json
import requests

class BaseRequest:
    def get_request(self, base_url, method_url, query = {}):
        url = base_url + method_url
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.get(url=url, params=query, headers=headers)
            return response
        except requests.RequestException as e:
            print(f'Ошибка отправки GET запроса: {str(e)}')

    def post_request(self, api_url, method_url, query = {}, data = {}):
        url = api_url + method_url
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url=url, params=query, data=json.dumps(data), headers=headers)
            return response
        except requests.RequestException as e:
            print(f'Ошибка отправки POST запроса: {str(e)}')

    def delete_request(self, api_url, method_url, query = {}, data = {}):
        url = api_url + method_url
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url=url, params=query, data=json.dumps(data), headers=headers)
            return response
        except requests.RequestException as e:
            print(f'Ошибка отправки DELETE запроса: {str(e)}')