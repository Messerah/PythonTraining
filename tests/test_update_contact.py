from model.Contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                    company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                      company="JSC", address="TroloLand", email="trolo@yandex.ru")

    contact.id = old_contacts[0].id
    app.contact.update(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
