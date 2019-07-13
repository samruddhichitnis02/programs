import clinic

def user():
    try:
        c = clinic.Clinic_Management()
        choice=int(input('1 to register 2 to update your details 3 to search doctor by name'
                     '4 to search doctor by specialization 5 to search doctor by availability 6 to take appoinment'
                     '7 to return to the menu  8 to exit -'))
        if(choice==1):
            c.register()
        elif(choice==2):
            c.update_user()
        elif(choice==3):
            c.search_by_name()
        elif(choice==4):
            c.specialization()
        elif(choice==5):
            c.availability()
        elif(choice==6):
            c.appointment()
        elif(choice==7):
            user()
        elif(choice==8):
            pass
        else:
            print('Invalid Choice!')
    except:
        raise ValueError
        #print('Invalid Input Please enter numbers only!')

user()