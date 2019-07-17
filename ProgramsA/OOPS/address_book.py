import address

c=address.Address_Book()
def user():
    try:
        print('Enter 1 to add account')
        print('2 to update user account')
        print('3 to delete user account')
        print('4 to print address book')
        print('5 to sort by pincode')
        print('6 to sort address book by name')
        print('7 to exit')
        choice = int(input())
        if (choice == 1):
            c.add_user_info()
            user()
        elif (choice == 2):
            c.update_user()
            user()
        elif (choice == 3):
            c.delete_user()
            user()
        elif (choice == 4):
            c.print_book()
            user()
        elif (choice == 5):
            c.sort_by_pincode()
            user()
        elif (choice == 6):
            c.sort_by_name()
            user()
        elif(choice==7):
            pass
        else:
            print('Invalid Input')
    except:
        print('Invalid Input!')


user()
