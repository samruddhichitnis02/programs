import address

c=address.Address_Book()
try:
    choice = int(input('Enter 1 to add account 2 to update user account 3 to delete user account'
                       ' 4 to print address book 5 to sort by pincode 6 to sort address book by name 7 to exit-'))
    if (choice == 1):
        c.add_user_info()
    elif (choice == 2):
        c.update_user()
    elif (choice == 3):
        c.delete_user()
    elif (choice == 4):
        c.print_book()
    elif (choice == 5):
        c.sort_by_pincode()
    elif (choice == 6):
        c.sort_by_name()
    elif(choice==7):
        pass
    else:
        print('Invalid Input')
except:
     print('Invalid Input!')



