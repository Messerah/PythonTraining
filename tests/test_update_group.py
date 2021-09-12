from model.Group import Group


def test_update_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    app.group.update_first_group(Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter"))


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    app.group.update_first_group(Group(header="Updatedheader22"))


def test_update_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    app.group.update_first_group(Group(footer="Updatedfooter22"))


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    app.group.update_first_group(Group(name="Updatedname22"))
