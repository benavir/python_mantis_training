from model.project import Project
import random


def test_delete_some_project(app, check_ui):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    if len(app.get_contact_list()) == 0:
        app.project.create_project(Project(name="delete"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.contact.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)