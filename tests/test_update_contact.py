from model.Contact import Contact


def test_update_first_contact(app):
    app.session.login()
    app.contact.update(
        Contact(firstname="Updated", middlename="Updated", lastname="Updated", nickname="Updated", title="Updated",
                company="Updated", address="Updated", email="trolo@yandex.ru"))
    app.session.logout()
