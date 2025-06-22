import allure
from pages.modal_page import ModalPage

@allure.epic("Модальное окно ингредиента")
class TestIngredientModal:

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_open_and_close_modal(self, driver):
        page = ModalPage(driver)
        page.click_first_ingredient()
        assert page.modal_is_open()
        page.close_modal()
        assert page.modal_is_closed()