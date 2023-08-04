from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        with allure.step('Ввести логин'):
            wd.find_element(By.NAME, "username").clear()
            wd.find_element(By.NAME, "username").send_keys(username)
        with allure.step('Ввести пароль'):
            wd.find_element(By.NAME, "password").clear()
            wd.find_element(By.NAME, "password").send_keys(password)
        with allure.step('Нажать кнопку Login'):
            wd.find_element(By.XPATH, '//input[@value="Login"]').click()

    def find_logout_link(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout")
    def find_login_form(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "login_form"))


    def logout(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку Logout'):
            wd.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.NAME, "username"))
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        user = self.get_logged_user()
        return user == username

    def get_logged_user(self):
        wd = self.app.wd
        user = wd.find_element(By.CSS_SELECTOR, "td.login-info-left span").text
        return user

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)





