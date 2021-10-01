from model.Contact import Contact


def test_update_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                    company="JSC", address="TroloLand", email="trolo@yandex.ru"))
    app.contact.update(
        Contact(firstname="Updated", middlename="Updated", lastname="Updated", nickname="Updated", title="Updated",
                company="Updated", address="Updated", email="trolo@yandex.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


