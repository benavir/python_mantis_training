from model.project import Project
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(symbols) for i in range(maxlen))


def test_add_project(app, check_ui):
    # app.session.login("administrator", "root")
    # assert app.session.is_logged_in_as("administrator")
    project = Project(name=random_string(5), description=random_string(10))
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_projects_list("administrator", "root")
    app.project.create_project(project)
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    if check_ui:
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
        # assert sorted(old_projects, key=lambda prj: prj.name) == sorted(new_projects, key=lambda prj: prj.name)
