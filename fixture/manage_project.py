from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from model.project import Project
from datetime import datetime
import re


class ManageProjectPageHelper:
    def __init__(self, app):
        self.app = app
    def create_new_project(self, project):
        self.init_create_new_project()
        self.fill_project_fields(project)
        self.submit_create_project()

    def init_create_new_project(self):
        wd = self.app.wd
        with allure.step('Нажать Create New Project'):
            wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
            WebDriverWait(wd, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Add Project')]")))

    def fill_project_fields(self, project):
        wd = self.app.wd
        with allure.step('Ввести уникальный Project Name'):
            wd.find_element(By.NAME, "name").send_keys(project.project_name)

    def submit_create_project(self):
        wd = self.app.wd
        with allure.step('Нажать Create New Project'):
            wd.find_element(By.XPATH, "//input[@type='submit' and @value='Add Project']").click()
            WebDriverWait(wd, 5).until(expected_conditions.invisibility_of_element_located((By.XPATH, "//td[contains(text(), 'Add Project')]")))
