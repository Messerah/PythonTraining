from random import randrange

from model.Contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                    company="JSC", address="TroloLand", email="trolo@yandex.ru", homephone=123456, mobilephone=00000,
                    workphone=123123213))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                      company="JSC", address="TroloLand", email="trolo@yandex.ru", homephone=123456, mobilephone=00000,
                      workphone=123123213)

    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
