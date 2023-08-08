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

def test_del_project_with_soap(app, db):

    # тестовые данные
    project_name = clear(str(datetime.now().time()))
    project = Project(project_name=project_name)

    # открыть главную страницу
    app.open_home_page()

    # открыть страницу с проектами
    app.manage_page.open_manage_page()
    app.manage_page.open_manage_projects()

    # если нет проектов, то добавить новый
    if len(db.get_project_list()) == 0:
        app.manage_project.create_new_project(project)

    # получить список проектов до удаления
    old_projects_list = db.get_project_list()
    old_projects_list_soap = app.soap.soap_mc_projects_get_user_accessible()

    #выбрать проект
    selected_project = random.choice(old_projects_list)
    #index = selected_project.id

    # удалить проект
    app.manage_project.delete_project(selected_project)

    # получить список проектов после удаления проекта
    new_projects_list_soap = app.soap.soap_mc_projects_get_user_accessible()

    assert len(new_projects_list_soap)+1 == len(old_projects_list_soap), \
        "Количество проектов до удаления не совпадает с количеством после удаления"

    # проверить что проект с таким названием отсутствует
    str_new_projects_list_soap = str(new_projects_list_soap)
    assert selected_project.project_name not in str_new_projects_list_soap

    #old_projects_list.remove(selected_project)

    #assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max), \
    #    "Спискок проектов до удаления не совпадает со списком после удаления"


def clear(s):
    return re.sub("[() - : .]", "", s)