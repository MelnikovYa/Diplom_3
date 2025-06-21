import allure
from pages.constructor_page import ConstructorPage
from locators.base_locators import OVERLAY
from locators.constructor_locators import CONSTRUCTOR_TAB

@allure.epic('Проверка конструктора')
class TestConstructor:

    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        page = ConstructorPage(driver)
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        page.base.wait_for_element_hide(OVERLAY)
        page.base.click(CONSTRUCTOR_TAB)
        assert page.is_constructor_url()

    @allure.title('При добавлении ингредиента в заказ счётчик увеличивается')
    def test_ingredient_counter_increments(self, driver):
        page = ConstructorPage(driver)
        count_before = page.get_ingredient_counter()
        page.drag_first_ingredient_to_cart()
        count_after = page.get_ingredient_counter()
        assert count_after in [count_before + 1, count_before + 2]