from random import randrange

from model.Group import Group


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
