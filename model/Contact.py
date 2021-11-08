from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, email=None, email2=None, email3=None, all_emails_from_homepage=None, id=None,
                 homephone=None, workphone=None, mobilephone=None, all_phones_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
