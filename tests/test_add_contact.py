# -*- coding: utf-8 -*-


from model.Contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                      company="JSC", address="TroloLand", email="trolo@yandex.ru", homephone=123456, mobilephone=00000,
                      workphone=123123213)
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_create_empty_contact(app):
# old_contacts = app.contact.get_contact_list()
# app.contact.create(
# Contact(firstname="", middlename="", lastname="", nickname="", title="",
# company="", address="", email=""))
# new_contacts = app.contact.get_contact_list()
# assert len(old_contacts) + 1 == len(new_contacts)
