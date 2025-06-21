import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по элементу')
    def click(self, locator):
        self.wait_for_element_hide((By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"))
        self.driver.find_element(*locator).click()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента')
    def is_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Получить элемент')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Получить список элементов')
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Подождать появления элемента')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
