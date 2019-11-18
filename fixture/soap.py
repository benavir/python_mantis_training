from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_list = client.service.mc_projects_get_user_accessible(username=username, password=password)
        names = []
        for elements in projects_list:
            names = elements.name
        # тут надо чтобы возвращался список названий групп а не список (буквы) последней группы
        return list(names)
        # return list(client.service.mc_projects_get_user_accessible(username=username, password=password))
