# -*- coding: utf-8 -*-


from model.Contact import Contact


def test_create_contact(app):
    app.contact.create(
        Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                company="JSC", address="TroloLand", email="trolo@yandex.ru"))


def test_create_empty_contact(app):
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="",
                company="", address="", email=""))
