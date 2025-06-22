from selenium.webdriver.common.by import By

MODAL_INGREDIENT = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6[draggable='true']")
MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")