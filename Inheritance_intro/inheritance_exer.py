class ContactList(list):
    def search(self,name):
        return [contact for contact in self if  name in contact.name]



class Contact:

    all_contacts = ContactList()

    def __init__(self,name,email,**kwgs):
        super().__init__(**kwgs) #inherits from object
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):

    def order(self,order):
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )


class AddressHolder(object):
    '''class to add address details to other classes'''
    def __init__(self,street='',city='',state='',code='',**kwgs):
        super().__init__(**kwgs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):

    def __init__(self, phone="",**kwgs):
        super().__init__(**kwgs)
        self.phone = phone


class MailSender(object):

    def send_mail(self,message):
        print('Mail has been sent to {addressee}: {msg}'.format(addressee = self.email,msg = message))


#as an alternative to MailSender:
def send_mail(Contact_obj, message):

    email = Contact_obj.email
    print('Mail has been sent to {addressee}: {msg}'.format(addressee=email, msg=message))


class EmailableContact(Contact, MailSender):
    pass

e = EmailableContact("John Smith", "jsmith@example.net")


class LongNameDct(dict):
    def get_longest_value(self):
        return sorted([(len(value),key) for key,value in self.items()], key=lambda x:x[0])[-1][-1]

    def get_longest_key(self):
        longest = ''

        for key in self.keys():
            if len(str(key)) >= len(longest):
                longest = str(key)

        return longest

c = Contact('Piotr','piotrbrendan')
s = Supplier('Arel','arelmax')

isinstance(ContactList,object)
isinstance(Contact.all_contacts,list)

d = LongNameDct({1:'zw',
                 3:'wwww'})
d
