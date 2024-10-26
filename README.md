Установка зависимостей pip3 install -r requirements.txt
Команда для запуска тестов с отчетом 
pytest --alluredir=allure_results 
Просмотр отчета 
allure serve allure_results
-s печатать print
-v подробный лог
pytest -v -s --alluredir=allure_results 