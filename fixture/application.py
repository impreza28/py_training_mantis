import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.manage_pages import ManagePageHelper
from fixture.manage_project import ManageProjectPageHelper
from fixture.soap import SoapHelper
import allure



class Application:
    def __init__(self, browser,base_url):

        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Не указан браузер")


        self.vars = {}
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.manage_page = ManagePageHelper(self)
        self.manage_project = ManageProjectPageHelper(self)
        self.soap = SoapHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        with allure.step('Открытие страницы mantis'):
            self.wd.get(self.base_url)
        with allure.step('Открытие окна браузера на полный экран'):
            self.wd.maximize_window()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
