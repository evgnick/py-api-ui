import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from config.data import Data


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {Data.HOST} page"):
            self.driver.get(Data.HOST)

    def make_screenshot(self, screenshot_name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
