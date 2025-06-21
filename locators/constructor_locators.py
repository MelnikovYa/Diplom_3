from selenium.webdriver.common.by import By

INGREDIENT = (By.XPATH, "//ul[contains(@class,'BurgerIngredients_ingredients__list')]/a[1]")
COUNTER = (By.XPATH, "//ul[contains(@class,'BurgerIngredients_ingredients__list')]/a[1]//p[contains(@class, 'counter_counter__num')]")
CART = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")