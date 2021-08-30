# Another homework is ready!!!
import pytest

from fixture.application import Application
from model.Group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login()
    app.group.create(Group(name="NewTestGroup", header="header", footer="footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
