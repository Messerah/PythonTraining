from model.Group import Group


def test_update_group(app):
    app.session.login()
    app.group.update(Group(name="UpdatedGroup", header="Updatedheader", footer="updatedfooter"))
    app.session.logout()

