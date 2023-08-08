
def test_soap(app):
    b = app.soap.can_login("administrator", "root")
    print(b)

def test_(app):
    app.soap.get_base_url()