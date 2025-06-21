import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть по элементу')
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)