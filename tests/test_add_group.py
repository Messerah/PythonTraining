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
    app.login()
    app.create_new_group(Group(name="NewTestGroup", header="header", footer="footer"))
    app.logout()


def test_add_empty_group(app):
    app.login()
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
