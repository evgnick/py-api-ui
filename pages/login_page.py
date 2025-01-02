import allure

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(ec.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(ec.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

