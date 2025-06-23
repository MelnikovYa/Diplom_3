import allure
from locators.modal_locators import *
from locators.base_locators import OVERLAY
from pages.base_page import BasePage

class ModalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть по первому ингредиенту')
    def click_first_ingredient(self):
        self.click(MODAL_INGREDIENT)

    @allure.step('Модалка открыта')
    def modal_is_open(self):
        return self.get_element(MODAL).is_displayed()

    @allure.step('Закрыть модалку')
    def close_modal(self):
        self.click(CLOSE_BUTTON)

    @allure.step('Кликнуть по первому ингредиенту')
    def click_first_ingredient(self):
        self.wait_for_element_hide(OVERLAY)
        self.wait_for_element(MODAL_INGREDIENT)
        self.click(MODAL_INGREDIENT)

    @allure.step("Проверить, что модалка закрыта")
    def modal_is_closed(self):
        self.wait_for_element_hide(MODAL)
        return True
