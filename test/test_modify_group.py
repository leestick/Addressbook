__author__ = 'ioK'
from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New Group1"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New Header1"))
