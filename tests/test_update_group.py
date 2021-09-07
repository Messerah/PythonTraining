from model.Group import Group


def test_update_group(app):
    app.group.update_first_group(Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter"))


def test_update_group_header(app):
    app.group.update_first_group(Group(header="Updatedheader22"))


def test_update_group_footer(app):
    app.group.update_first_group(Group(footer="Updatedfooter22"))


def test_update_group_name(app):
    app.group.update_first_group(Group(name="Updatedname22"))
