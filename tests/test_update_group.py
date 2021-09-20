from model.Group import Group


def test_update_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(header="Updatedheader22"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(footer="Updatedfooter22"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="Updatedname22"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
