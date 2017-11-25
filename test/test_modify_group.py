__author__ = 'ioK'


def test_modify_first_group_name(app):
    app.session.user_login(username="admin", password="secret")
    app.group.modify(name="New Group1")
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.user_login(username="admin", password="secret")
    app.group.modify(header="New Header1")
    app.session.logout()
