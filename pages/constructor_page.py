import allure
from locators.constructor_locators import FEED_TAB, COUNTER, INGREDIENT, CART, CONSTRUCTOR_TAB
from locators.base_locators import OVERLAY
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть страницу фида и перейти в конструктор')
    def open_feed_and_go_to_constructor(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")
        self.wait_for_element_hide(OVERLAY)
        self.click(CONSTRUCTOR_TAB)

    @allure.step('Нажать на таб "Лента заказов"')
    def click_feed(self):
        self.click(FEED_TAB)

    @allure.step('Получить счётчик ингредиента')
    def get_ingredient_counter(self):
        self.wait_for_element(COUNTER)
        return int(self.get_text(COUNTER))

    @allure.step('Перетащить первый ингредиент в корзину')
    def drag_first_ingredient_to_cart(self):
        ingredient = self.get_element(INGREDIENT)
        cart = self.get_element(CART)
        self.drag_and_drop_element(ingredient, cart)

    @allure.step('Проверить, что открыт конструктор')
    def is_constructor_url(self):
        return "/constructor" in self.driver.current_url or self.driver.current_url.rstrip("/") == "https://stellarburgers.nomoreparties.site"