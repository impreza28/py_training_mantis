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

    def open_project(self, project_name):
        wd = self.app.wd
        with allure.step('Нажать на ссылку с названием проекта'):
            WebDriverWait(wd, 10).until(expected_conditions.element_to_be_clickable(
                (By.LINK_TEXT, f"{project_name}")))
            wd.find_element(By.LINK_TEXT, f"{project_name}").click()
            WebDriverWait(wd, 10).until(expected_conditions.presence_of_element_located(
                (By.NAME, "project_id")))

    def submit_delete_project(self):
        wd = self.app.wd
        with allure.step('Подтвердить удаление'):
            wd.find_element(By.XPATH, "//form[@action='manage_proj_delete.php']//input[@value='Delete Project']").click()
            WebDriverWait(wd, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//table[@class='width100']//td[@class='form-title']")))
    def init_delete_project(self):
        wd = self.app.wd
        with allure.step('Нажать кнопку удаления проекта'):
            wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
            WebDriverWait(wd, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//form[@action='manage_proj_delete.php']//input[@value='Delete Project']")))

    def delete_project(self, project):
        self.open_project(project.project_name)
        self.init_delete_project()
        self.submit_delete_project()




