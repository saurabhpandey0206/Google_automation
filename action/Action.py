from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        am_title = self.driver.title
        return am_title
