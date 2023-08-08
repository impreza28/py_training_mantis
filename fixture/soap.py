from suds.client import Client
from suds import WebFault
import json


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login (self, username, password):
        client = Client(f"{self.app.base_url}/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def soap_project_get_id_from_name (self, username, password, project_name):
        client = Client(f"{self.app.base_url}/api/soap/mantisconnect.php?wsdl")
        try:
            a = client.service.mc_project_get_id_from_name(username, password, project_name)

            return True
        except WebFault:
            return False

    def soap_mc_projects_get_user_accessible (self):
        client = Client(f"{self.app.base_url}/api/soap/mantisconnect.php?wsdl")
        try:
            a = client.service.mc_projects_get_user_accessible(self.app.username, self.app.password)
            return a
        except WebFault:
            return False

