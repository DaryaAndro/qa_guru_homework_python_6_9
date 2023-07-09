import allure

from selene import browser, be, by
from allure_commons.types import Severity

@allure.tag("Web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Issues are displayed in the repository")
@allure.story("Issues in the repository are displayed to the authorized user")
@allure.link("https://github.com/DaryaAndro", name="Darya Andronova")
def test_dynamic_steps():
    with allure.step("Открыть главную страницу github"):
        browser.open("https://github.com")

    with allure.step("Поиск репозитория"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").type("eroshenkoam/allure-example").press_enter()

    with allure.step("Перейти по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открыть таб Issue"):
        browser.element("#issues-tab").click()

    with allure.step("Проверить наличие Issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)

