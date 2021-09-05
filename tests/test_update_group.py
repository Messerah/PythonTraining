from model.Group import Group


def test_update_group(app):
    app.session.login()
    app.group.update_first_group(Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter"))
    app.session.logout()


def test_update_group_header(app):
    app.session.login()
    app.group.update_first_group(Group(header="Updatedheader22"))
    app.session.logout()


def test_update_group_footer(app):
    app.session.login()
    app.group.update_first_group(Group(footer="Updatedfooter22"))
    app.session.logout()

def test_update_group_name(app):
    app.session.login()
    app.group.update_first_group(Group(name="Updatedname22"))
    app.session.logout()
