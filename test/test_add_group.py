# -*- coding: utf-8 -*-
#from group import Group


def test_group_add_unittest(app):
    app.session.user_login(username="admin", password="secret")
    app.group.create(name="Group1", header="Header1", footer="Footer1")
    app.session.logout()


def test_empty_group_add_unittest(app):
    app.session.user_login(username="admin", password="secret")
    app.group.create(name="", header="", footer="")
    app.session.logout()




