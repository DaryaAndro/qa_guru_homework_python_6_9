import allure

from selene import browser, be, by
from allure_commons.types import Severity


@allure.tag("Web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Issues отображается в репозитории")
@allure.story("Авторизованному пользователю отображаются Issues в репозитории ")
@allure.link("https://github.com/DaryaAndro", name="Darya Andronova")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открыть главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type(repo).press_enter()


@allure.step("Перейти по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открыть таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
