__author__ = 'ioK'

def test_delete_first_group(app):
    app.session.user_login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()