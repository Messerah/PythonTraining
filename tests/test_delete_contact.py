# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.session.login()
    app.contact.delete()
    app.session.logout()
