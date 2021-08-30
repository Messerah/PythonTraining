# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.Contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login()
    app.contact.create(
        Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    app.session.logout()


def test_create_empty_contact(app):
    app.session.login()
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="",
                company="", address="", email=""))
    app.session.logout()
