from selenium.webdriver.common.by import By

INGREDIENT = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6[draggable='true']")
COUNTER = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6[draggable='true'] p.counter_counter__num__3nue1")
CART = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")