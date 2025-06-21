import allure
from locators.feed_locators import *
from pages.base_page import BasePage

class FeedPage:

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    @allure.step('Получить значение "Выполнено за всё время"')
    def get_total_done(self):
        return int(self.base.get_text(TOTAL_DONE))

    @allure.step('Получить значение "Выполнено за сегодня"')
    def get_today_done(self):
        return int(self.base.get_text(TODAY_DONE))