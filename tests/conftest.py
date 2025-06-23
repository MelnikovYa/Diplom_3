import pytest
from selenium import webdriver
from data.config import main_site

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(main_site)
    yield driver
    driver.quit()
