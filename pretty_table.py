from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Last name', 'First name', 'Country', 'Gender', 'Phone number']
table.add_row(['Kurbanov', 'Timur', 'Tashkent', 'Male', '+998(33)902-30-02'])
table.align = 'c'

print(table)
