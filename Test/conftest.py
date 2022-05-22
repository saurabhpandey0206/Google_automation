import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
        driver.get("https://www.amazon.in/")
        driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()