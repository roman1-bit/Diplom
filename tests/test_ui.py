import allure
from config.config import BASE_URL
from pages.SearchPage import SearchPage
from pages.MoviePage import MoviePage


@allure.feature("UI Tests")
@allure.story("Поиск фильма по названию")
def test_search_movie(driver, valid_movie):
    with allure.step("Открыть главную страницу"):
        search_page = SearchPage(driver)
        search_page.open(BASE_URL)

    with allure.step(f"Искать фильм '{valid_movie}'"):
        search_page.search(valid_movie)

    with allure.step("Проверить, что первый результат содержит название"):
        first_result = search_page.get_first_film_text()
        assert valid_movie.lower() in first_result.lower()


@allure.feature("UI Tests")
@allure.story("Поиск сериала по названию")
def test_search_series(driver, series_name):
    with allure.step("Открыть главную страницу"):
        search_page = SearchPage(driver)
        search_page.open(BASE_URL)

    with allure.step(f"Искать фильм '{series_name}'"):
        search_page.search(series_name)

    with allure.step("Проверить, что первый результат содержит название"):
        first_result = search_page.get_first_series_text()
        assert series_name.lower() in first_result.lower()


@allure.feature("UI Tests")
@allure.story("Поиск фильма с несуществующим названием")
def test_search_invalid_movie(driver, invalid_movie):
    search_page = SearchPage(driver)
    search_page.open(BASE_URL)

    with allure.step("Ввести несуществующее название"):
        search_page.search(invalid_movie)

    with allure.step("Проверить, что результатов нет"):
        invalid_result = search_page.number_results_text()
        assert "результаты: 0" in invalid_result.lower()


@allure.feature("UI Tests")
@allure.story("Открытие карточки фильма")
def test_open_movie_card(driver, valid_movie):
    search_page = SearchPage(driver)
    search_page.open(BASE_URL)

    with allure.step("Искать фильм"):
        search_page.search(valid_movie)
        search_page.click_first_result()

    with allure.step("Проверить, что заголовок фильма отображается"):
        movie_page = MoviePage(driver)
        assert valid_movie.lower() in movie_page.get_title().lower()


@allure.feature("UI Tests")
@allure.story("Поиск актера через поиск")
def test_search_actor_first_result(driver, actor_name):
    search_page = SearchPage(driver)
    search_page.open(BASE_URL)

    with allure.step("Ввести имя актера в строку поиска"):
        search_page.search(actor_name)

    with allure.step("Убедиться, что первый результат — это Петров"):
        first_result = search_page.get_first_person_text()
        assert actor_name.lower() in first_result.lower()
