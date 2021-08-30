# -*- coding: utf-8 -*-

import pytest

from contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login()
    app.create_new_contact(
        Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    app.session.logout()


def test_create_empty_contact(app):
    app.session.login()
    app.create_new_contact(
        Contact(firstname="", middlename="", lastname="", nickname="", title="",
                company="", address="", email=""))
    app.session.logout()
