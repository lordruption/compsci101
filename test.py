contact_list = [('Ann Cameron', '022-7654321', 'ann@bmail.com'),
                 ('Damir Azhar', '021-1234567', 'damir@emailprovider.com')]

flat_contact_list = [item for contact in contact_list for item in contact]


print(flat_contact_list)