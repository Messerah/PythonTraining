from model.Contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                    company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Updated", middlename="Updated", lastname="Updated", nickname="Updated",
                      title="Updated",
                      company="Updated", address="Updated", email="trolo@yandex.ru")
    app.contact.update(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
