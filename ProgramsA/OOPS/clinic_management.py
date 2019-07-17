import clinic

def user():
    try:
        c = clinic.Clinic_Management()
        print('Enter 1 if you want to search a doctor and 2 if you want to search a patient 3 to exit-')
        choice=int(input())
        if(choice==1):
            print('1 to search doctor by specialization ')
            print('2 to search doctor by availability')
            print('3 to search doctor by name')
            choice1=int(input())
            if(choice1==1):
                c.specialization()
            elif(choice1==2):
                c.availability()
            elif (choice1 == 3):
                c.search_by_name()
            else:
                print('Invalid option')
            print('Do You want to take appointment Enter Y/N')
            choice2=input()
            if(choice2=='Y'):
                c.appointment()
            user()
        elif(choice==2):
            print('Enter 1 to register  and 2 to update your credentials=')
            choice3=int(input())
            if(choice3==1):
                c.register()
            elif(choice3==2):
                c.update_user()
                user()
        elif(choice==3):
            pass
        else:
            print('Invalid Choice!')
    except:
        raise ValueError
        #print('Invalid Input Please enter numbers only!')
        #user()

user()