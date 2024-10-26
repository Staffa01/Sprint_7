import json
import requests

class BaseRequest:
    def get_request(self, token=None, base_url="", method_url="",query = {}):
        url = base_url + method_url
        if token != None:
            headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        else:
            headers = {'Content-Type': 'application/json'}
        try:
            response = requests.get(url=url, params=query, headers=headers)
            return response
        except requests.RequestException as e:
            print(f'Ошибка отправки GET запроса: {str(e)}')

    def post_request(self, token=None, api_url="",method_url="",query = {},data = {}):
        url = api_url + method_url
        if token != None:
            headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        else: headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url=url, params=query, data=json.dumps(data), headers=headers)
            return response
        except requests.RequestException as e:
            print(f'Ошибка отправки POST запроса: {str(e)}')