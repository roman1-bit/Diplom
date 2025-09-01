import allure
import pytest
import json
from selenium import webdriver
from config.config import BASE_URL_API, KINOPOISK_API_KEY


@pytest.fixture(scope="session")
def driver():
    """Фикстура для создания WebDriver с автоматическим закрытием
    после сессии"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    web_driver = webdriver.Chrome()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def valid_movie():
    """Валидное название фильма для поиска"""
    return "1+1"


@pytest.fixture
def invalid_movie():
    """Невалидное название фильма для поиска"""
    return "авыжаыв"


@pytest.fixture
def series_name():
    """Название сериала для поиска"""
    return "Чикатило"


@pytest.fixture
def actor_name():
    """Имя актера для поиска"""
    return "Петров"


@pytest.fixture
def api_headers():
    """Стандартные заголовки для API запросов"""
    return {
        "accept": "application/json",
        "X-API-KEY": KINOPOISK_API_KEY
    }


@pytest.fixture
def invalid_api_headers():
    """Заголовки с невалидным API ключом"""
    return {
        "accept": "application/json",
        "X-API-KEY": "INVALID_API_KEY"
    }


@pytest.fixture
def api_base_url():
    """Базовый URL для API"""
    return BASE_URL_API


def attach_json(data, name):
    """Функция для прикрепления JSON данных к отчету Allure"""
    allure.attach(json.dumps(data, indent=2),
                  name, allure.attachment_type.JSON)


def attach_response_info(response):
    """Функция для прикрепления информации о HTTP ответе к отчету Allure"""
    allure.attach(f"Response URL: {response.url}",
                  "Request URL", allure.attachment_type.TEXT)
    allure.attach(f"Status Code: {response.status_code}",
                  "Response Status Code", allure.attachment_type.TEXT)
    try:
        attach_json(response.json(), "Response JSON")
    except (ValueError, TypeError):
        allure.attach(response.text, "Response Text",
                      allure.attachment_type.TEXT)
