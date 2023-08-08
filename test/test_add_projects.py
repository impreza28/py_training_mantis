from model.project import Project
from datetime import datetime
import re
import os
import json


def test_add_new_project(app, db):

    # тестовые данные
    project_name = 'Autotest' + f'{clear(str(datetime.now().time()))}'
    project = Project(project_name=project_name)

    # открыть главную страницу
    app.open_home_page()

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

def test_add_new_project_with_soap_check(app):

    # тестовые данные
    project_name = 'Autotest' + f'{clear(str(datetime.now().time()))}'
    project = Project(project_name=project_name)

    # открыть главную страницу
    app.open_home_page()

    # открыть страницу с проектами
    app.manage_page.open_manage_page()
    app.manage_page.open_manage_projects()

    # получить список проектов до добавления нового
    old_projects_list = app.soap.soap_mc_projects_get_user_accessible()
    # проверить что проекта с таким названием нет
    str_old_projects_list = str(old_projects_list)
    assert project_name not in str_old_projects_list

    # добавить новый проект
    app.manage_project.create_new_project(project)
    # получить список проектов после добавления нового проекта
    new_projects_list = app.soap.soap_mc_projects_get_user_accessible()

    assert len(new_projects_list)-1 == len(old_projects_list), \
        "Количество проектов до добавления не совпадает с количеством после добавления"

    # проверить что проект с таким названием есть
    str_new_projects_list = str(new_projects_list)
    assert project_name in str_new_projects_list
    #old_projects_list.append(project)

    #assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max), \
    #    "Спискок проектов до добавления не совпадает со списком после добавления"


def clear(s):
    return re.sub("[() - : .]", "", s)