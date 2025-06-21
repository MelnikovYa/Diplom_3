import allure
from locators.constructor_locators import FEED_TAB, COUNTER, INGREDIENT, CART
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConstructorPage:

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    @allure.step('Нажать на таб "Лента заказов"')
    def click_feed(self):
        self.base.click(FEED_TAB)

    @allure.step('Получить счётчик ингредиента')
    def get_ingredient_counter(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(COUNTER))
        return int(self.base.get_text(COUNTER))

    @allure.step('Перетащить первый ингредиент в корзину')
    def drag_first_ingredient_to_cart(self):
        ingredient = self.driver.find_element(*INGREDIENT)
        cart = self.driver.find_element(*CART)
        self.base.drag_and_drop_element(ingredient, cart)

    @allure.step('Проверить, что открыт конструктор')
    def is_constructor_url(self):
        return "/constructor" in self.driver.current_url or self.driver.current_url.rstrip("/") == "https://stellarburgers.nomoreparties.site"