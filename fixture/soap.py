from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        # client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        # client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_list = client.service.mc_projects_get_user_accessible(username=username, password=password)
        self.projects = []
        for elements in projects_list:
            ids = elements.id
            names = elements.name
            descriptions = elements.description
            self.projects.append(Project(id=ids, name=names, description=descriptions))
        return list(self.projects)
        # return list(client.service.mc_projects_get_user_accessible(username=username, password=password))
