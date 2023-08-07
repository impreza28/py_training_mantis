
def test_soap(app):
    b = app.soap.soap_mc_projects_get_user_accessible("administrator", "root")
    print(b)