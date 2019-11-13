from model.project import Project
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(symbols) for i in range(maxlen))


def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    project = Project(name=random_string(5), description=random_string(10))
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)