import allure
from pages.feed_page import FeedPage
from locators.base_locators import OVERLAY

@allure.epic('Проверка UI функциональности')
class TestFeed:

    @allure.title('Проверка роста счётчика "Выполнено за все время"')
    def test_total_orders_increases(self, driver):
        page = FeedPage(driver)
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        page.base.wait_for_element_hide(OVERLAY)
        count_before = page.get_total_done()
        driver.refresh()
        page.base.wait_for_element_hide(OVERLAY)
        count_after = page.get_total_done()
        assert count_after >= count_before

    @allure.title('Проверка роста счётчика "Выполнено за сегодня"')
    def test_today_orders_increases(self, driver):
        page = FeedPage(driver)
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        page.base.wait_for_element_hide(OVERLAY)
        count_before = page.get_today_done()
        driver.refresh()
        page.base.wait_for_element_hide(OVERLAY)
        count_after = page.get_today_done()
        assert count_after >= count_before
