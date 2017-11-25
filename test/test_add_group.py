# -*- coding: utf-8 -*-
import pytest
#from group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_add_unittest(app):
    app.user_login(username="admin", password="secret")
    app.create_group(name="Group1", header="Header1", footer="Footer1")
    app.logout()


def test_empty_group_add_unittest(app):
    app.user_login(username="admin", password="secret")
    app.create_group(name="", header="", footer="")
    app.logout()




