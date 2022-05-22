from selenium.webdriver.support.ui import WebDriverWait
import selenium
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from action.Action import Base


class Home(Base):

    def __init__(self, driver):
        super.__init__(driver)

    def get_t(self):
        return self.get_title()