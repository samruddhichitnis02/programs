import  json
class Clinic_Management:
    def __init__(self):
        self.data=' '
        self.y={ }

    def create(self):
        x={'Patients':[ ]}
        with open('patients.json','w') as f:
            json.dump(x,f,indent=2)
        f.close()

    def open_file(self):
        with open('patients.json','r') as f:
            self.data=json.load(f)
        f.close()

    def write_to_file(self):
        with open('patients.json','w') as f:
            json.dump(self.data,f,indent=2)
        f.close()

    def register(self):
        self.open_file()
        try:
            name=input('Enter your name-')
            if(name.isalpha()):
                cno=int(input('Enter your contact number-'))
                age=int(input('Enter your age-'))
                self.y['name']=name
                self.y['cno']=cno
                self.y['age']=age

            else:
                print('Invalid Input Enter proper name-')
            self.data['Patients'].append(self.y)
            self.write_to_file()
            print(self.data)
        except:
            raise ValueError
            #print('Invalid Input!')

    def update_user(self):
        self.open_file()
        try:
            name=input('Enter your name to update your details-')
            if(name.isalpha()):
                for i in range(len(self.data['Patients'])):
                    if(name==self.data['Patients'][i]['name']):
                        choice=int(input('Enter 1 to update your contact number & 2 to update your '
                                         'age 3 to change your doctor 4 to return to the menu 5 to exit-'))
                        if(choice==1):
                            try:
                                if (name == self.data['Patients'][i]['name']):
                                    cno=int(input('Enter your contact number to update-'))
                                    self.data['Patients'][i]['cno']=cno
                                else:
                                    print('Entered Name not found! Please try again !')
                                    self.update_user()
                            except:
                                print('Invalid Input Please enter numbers only!')
                        elif(choice==2):
                            try:
                                if (name == self.data['Patients'][i]['name']):
                                    age=int(input('Enter your age to update-'))
                                    self.data['Patients'][i]['age']=age
                                else:
                                    print('Entered Name not found! Please try again !')
                                    self.update_user()
                            except:
                                print('Invalid Input Please enter numbers only!')
                        elif(choice==3):
                            pass
                        elif(choice==4):
                            self.update_user()
                        elif(choice==5):
                            pass

                self.write_to_file()
            print(self.data)
        except:
            print('Invalid Input!')


    def search_by_name(self):
        try:
            with open('doctors.json','r') as f:
                data=json.load(f)

                name=input('Enter the name of the doctor-')
                if(name.isalpha()):
                    for i in range(len(data['doctors'])):
                        if(name==data['doctors'][i]['name']):
                            print(data['doctors'][i])

                    if (name != data['doctors'][i]['name']):
                        print('Doctor not found!')

                else:
                    print('Enter a valid name!')
            f.close()
        except:
            raise ValueError
            #print('Invalid Input!')

    def specialization(self):
        pass

    def availability(self):
        pass

    def appointment(self):
        pass

