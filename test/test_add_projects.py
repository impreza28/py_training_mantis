from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from model.project import Project
from datetime import datetime
import re


def test_add_new_project(app, db):

    # тестовые данные
    project_name = clear(str(datetime.now().time()))
    project = Project(project_name=project_name)

    # открыть главную страницу
    app.open_home_page()
    # если не залогинены, то авторизоваться
    if app.session.find_login_form() == 1:
        app.session.login("administrator", "root")

    # открыть страницу с проектами
    app.manage_page.open_manage_page()
    app.manage_page.open_manage_projects()

    # получить список проектов до добавления нового
    old_projects_list = db.get_project_list()
    # добавить новый проект
    app.manage_project.create_new_project(project)
    # получить список проектов после добавления нового проекта
    new_projects_list = db.get_project_list()

    assert len(new_projects_list)-1 == len(old_projects_list), \
        "Количество проектов до добавления не совпадает с количеством после добавления"

    old_projects_list.append(project)

    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max), \
        "Спискок проектов до добавления не совпадает со списком после добавления"


def clear(s):
    return re.sub("[() - : .]", "", s)



#    self.driver.find_element(By.NAME, "name").click()
#    self.driver.find_element(By.NAME, "name").send_keys("test")
#    self.driver.find_element(By.CSS_SELECTOR, ".button").click()
#    self.driver.find_element(By.CSS_SELECTOR, ".form-title .button-small").click()
#    self.driver.find_element(By.NAME, "name").click()
#    self.driver.find_element(By.NAME, "name").send_keys("sadsads")
#    self.driver.find_element(By.CSS_SELECTOR, ".button").click()
#    self.driver.find_element(By.LINK_TEXT, "Proceed").click()
#    self.driver.find_element(By.LINK_TEXT, "test").click()
#    self.driver.find_element(By.CSS_SELECTOR, "form > .button:nth-child(3)").click()
#    self.driver.find_element(By.CSS_SELECTOR, ".button").click()
