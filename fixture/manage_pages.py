from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from model.project import Project
from datetime import datetime
import re


class ManagePageHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        with allure.step('Открытие страницы manage_overview_page'):
            wd.find_element(By.LINK_TEXT, "Manage").click()
            WebDriverWait(wd, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "width75")))

    def open_manage_projects(self):
        wd = self.app.wd
        with allure.step('Открытие страницы Projects'):
            wd.find_element(By.LINK_TEXT, "Manage Projects").click()
            WebDriverWait(wd, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "width100")))








