import json
import requests

class BaseRequest:
    timeout = 40
    def get_request(self, base_url, method_url, query = {}):
        url = base_url + method_url
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.get(url=url, params=query, headers=headers, timeout=self.timeout)
            return response
        except requests.ConnectionError as e:
            print(f'Ошибка подключения:\n {str(e)}')
        except requests.Timeout as e:
            print(f'Ошибка тайм-аута:\n {str(e)}')
        except requests.RequestException as e:
            print(f'Ошибка запроса: \n {str(e)}')
        except requests.exceptions.RequestException:
            print(f'Необработанная ошибка: \n {str(e)}')
            raise SystemExit(e)
        

    def post_request(self, api_url, method_url, query = {}, data = {}):
        url = api_url + method_url
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url=url, params=query, data=json.dumps(data), headers=headers)
            return response
        except requests.ConnectionError as e:
            print(f'Ошибка подключения:\n {str(e)}')
        except requests.Timeout as e:
            print(f'Ошибка тайм-аута:\n {str(e)}')
        except requests.RequestException as e:
            print(f'Ошибка запроса: \n {str(e)}')
        except requests.exceptions.RequestException:
            print(f'Необработанная ошибка: \n {str(e)}')
            raise SystemExit(e)

    def delete_request(self, api_url, method_url, query = {}, data = {}):
        url = api_url + method_url
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url=url, params=query, data=json.dumps(data), headers=headers, timeout=self.timeout)
            return response
        except requests.ConnectionError as e:
            print(f'Ошибка подключения:\n {str(e)}')
        except requests.Timeout as e:
            print(f'Ошибка тайм-аута:\n {str(e)}')
        except requests.RequestException as e:
            print(f'Ошибка запроса: \n {str(e)}')
        except requests.exceptions.RequestException:
            print(f'Необработанная ошибка: \n {str(e)}')
            raise SystemExit(e)