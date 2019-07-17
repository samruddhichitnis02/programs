import commercial_data
def user():
    c=commercial_data.Customer()
    try:
        print('1 To register')
        print('2 To login')
        print('3 to Exit')
        choice=int(input( ))
        if(choice==1):
            c.register()
            user()
        elif (choice==2):
            c.login()
        elif(choice==3):
            pass
        else:
            print('Invalid Choice')
    except:
        print('Invalid Input!')
user()