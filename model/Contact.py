class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.middlename)

    def __eq__(self, other):
        return self.id == other.id and self.middlename == other.middlename, self.lastname == other.lastname
