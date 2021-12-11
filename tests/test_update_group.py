import random
import string

import pytest

from model.Group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 30))]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_update_group(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group = Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter")
    group.id = old_groups[index].id
    app.group.update_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
