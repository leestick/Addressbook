# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add_unittest(app):
    app.group.create(Group(name="Group1", header="Header1", footer="Footer1"))



def test_empty_group_add_unittest(app):
    app.group.create(Group(name="", header="", footer=""))




