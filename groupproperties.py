__author__ = 'Pavel Ageyev'
class Groups:
    def __init__(self, name , header, footer):
        self.name=name
        self.header=header
        self.footer=footer

class Formfields:
    def __init__(self,  firstName, lastName, companyName, email, mobile):
        self.firstName=firstName
        self.lastName=lastName
        self.companyName=companyName
        self.email=email
        self.mobile=mobile