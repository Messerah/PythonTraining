# -*- coding: utf-8 -*-


from model.Contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                      company="JSC", address="TroloLand", email="trolo@yandex.ru")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="",
                company="", address="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
