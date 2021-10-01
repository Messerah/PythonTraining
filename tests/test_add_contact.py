# -*- coding: utf-8 -*-


from model.Contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(
        Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="",
                company="", address="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

