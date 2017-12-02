__author__ = 'dmitryh'

from fixture.session import SessionHelper

def test_login(app):
    app.session.user_login("admin", "secret")
    app.session.logout()



