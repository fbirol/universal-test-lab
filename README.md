.\venv\Scripts\activate

cd app
python main.py

cd ..
pytest --alluredir=allure-results

allure serve allure-results


black .
isort .
flake8 .
