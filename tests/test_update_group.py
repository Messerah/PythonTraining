from random import randrange

from model.Group import Group


def test_update_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter")
    group.id = old_groups[index].id
    app.group.update_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

