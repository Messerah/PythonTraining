# -*- coding: utf-8 -*-


from model.Contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.count()
    app.contact.create(
        Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    new_contacts = app.contact.count()
    assert old_contacts + 1 == new_contacts


def test_create_empty_contact(app):
    old_contacts = app.contact.count()
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="",
                company="", address="", email=""))
    new_contacts = app.contact.count()
    assert old_contacts + 1 == new_contacts
