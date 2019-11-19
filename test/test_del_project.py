from model.project import Project
import random


def test_delete_some_project(app, check_ui):
    # app.session.login("administrator", "root")
    # assert app.session.is_logged_in_as("administrator")
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="delete"))
    old_projects = app.soap.get_projects_list("administrator", "root")
    # old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.soap.get_projects_list("administrator", "root")
    # new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
    if check_ui:
        assert sorted(old_projects, key=lambda prj: prj.name) == sorted(new_projects, key=lambda prj: prj.name)
