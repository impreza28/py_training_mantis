import random

from model.project import Project
from datetime import datetime
import re


def test_del_project(app, db):

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

    # если нет проектов, то добавить новый
    if len(db.get_project_list()) == 0:
        app.manage_project.create_new_project(project)

    # получить список проектов до удаления
    old_projects_list = db.get_project_list()

    #выбрать проект
    selected_project = random.choice(old_projects_list)
    #index = selected_project.id

    # удалить проект
    app.manage_project.delete_project(selected_project)

    # получить список проектов после удаления проекта
    new_projects_list = db.get_project_list()

    assert len(new_projects_list)+1 == len(old_projects_list), \
        "Количество проектов до удаления не совпадает с количеством после удаления"

    old_projects_list.remove(selected_project)

    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max), \
        "Спискок проектов до удаления не совпадает со списком после удаления"


def clear(s):
    return re.sub("[() - : .]", "", s)