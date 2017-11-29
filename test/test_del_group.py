__author__ = 'ioK'
from model.group import Group

def test_delete_first_group(app):
    # проверка есть ли хотя бы одна группа
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
