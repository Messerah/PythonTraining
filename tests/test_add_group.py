from model.Group import Group


def test_add_group(app):
    app.session.login()
    app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
