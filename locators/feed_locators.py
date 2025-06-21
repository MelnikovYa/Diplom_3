from selenium.webdriver.common.by import By

TOTAL_DONE = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large')]"
TODAY_DONE = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]"
IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]/li")