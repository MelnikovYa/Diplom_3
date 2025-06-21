import allure
from locators.modal_locators import *
from locators.base_locators import OVERLAY
from pages.base_page import BasePage

class ModalPage:

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    @allure.step('Кликнуть по первому ингредиенту')
    def click_first_ingredient(self):
        self.base.click(MODAL_INGREDIENT)

    @allure.step('Модалка открыта')
    def modal_is_open(self):
        return self.driver.find_element(*MODAL).is_displayed()

    @allure.step('Закрыть модалку')
    def close_modal(self):
        self.base.click(CLOSE_BUTTON)

    @allure.step('Проверка отсутствия модалки')
    def modal_is_present(self):
        elements = self.driver.find_elements(*MODAL)
        return len(elements) > 0