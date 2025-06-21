from selenium.webdriver.common.by import By

MODAL_INGREDIENT = (By.XPATH, "//section[contains(@class,'BurgerIngredients_ingredients__')]/div[1]//li[1]//a")
MODAL = (By.CLASS_NAME, "Modal_modal__")
CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3VxqZ")