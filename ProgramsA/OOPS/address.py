import json
class Address_Book:
    def __init__(self):
        self.data=' '
        self.y={ }

    def create(self):
        try:
            x = {"add_data": []}
            with open('address.json','w') as f:
               json.dump(x,f,indent=2)
            f.close( )
        except:
            print('File not found!')


    def open_file(self):
        with open('address.json','r') as f:
            self.data=json.load(f)
        f.close()

    def write_to_file(self):
        with open('address.json','w') as f:
            json.dump(self.data,f,indent=2)
        f.close()


    def add_user_info(self):
        try:
            self.open_file()
            f_name=input('Enter your first name-')
            l_name=input('Enter ypur last name-')
            cno=int(input('Enter your contact number-'))
            add=input('Enter your area-')
            city=input('Enter your city name-')
            pincode=int(input('Enter your pincode'))
            if(f_name.isalpha() and l_name.isalpha() and add.isalpha() and city.isalpha()):
                self.y['f_name']=f_name
                self.y['l_name']=l_name
                self.y['Contact Num']=cno
                self.y['address']=add
                self.y['city']=city
                self.y['pincode']=pincode
                self.data["add_data"].append(self.y)
                self.write_to_file()
            else:
                print('Invalid Input')
        except:
            print('Error!')
            self.add_user_info()

    def update_user(self):
        self.open_file()
        try:
            if(len(self.data)>0):
                f_name = input('Enter the firstname of user to update credentials-')
                if(f_name.isalpha()):
                    for i in range(len(self.data['add_data'])):
                        if(self.data['add_data'][i]['f_name']==f_name):
                            print(self.data['add_data'][i])
                            choice=int(input('Enter 1 to change the contact number 2 to change the area 3 to '
                           'change the city 4 to change the pincode'))
                            if (choice == 1):
                                if (self.data['add_data'][i]['f_name'] == f_name):
                                    cno = int(input('Enter your contact number to update-'))
                                    self.data['add_data'][i]['Contact Num'] = cno
                                    print(self.data['add_data'][i])
                                else:
                                    print('Name not found!')
                                break
                            elif (choice == 2):
                                if (self.data['add_data'][i]['f_name'] == f_name):
                                    add = input('Enter your area to update-')
                                    if (add.isalpha()):
                                        self.data['add_data'][i]['address'] = add
                                        print(self.data['add_data'][i])
                                else:
                                    print('Name not found!')
                                break
                            elif (choice == 3):
                                if (self.data['add_data'][i]['f_name'] == f_name):
                                    city = input('Enter your city to update-')
                                    if (city.isalpha()):
                                        self.data['add_data'][i]['city'] = city
                                        print(self.data['add_data'][i])
                                else:
                                    print('Name not found!')
                                break
                            elif (choice == 4):
                                if (self.data['add_data'][i]['f_name'] == f_name):
                                    pincode = int(input('Enter your contact number to update-'))
                                    self.data['add_data'][i]['pincode'] = pincode
                                    print(self.data['add_data'][i])
                                else:
                                    print('Name not found!')
                                break
                            else:
                                print('Invalid Option!')
                    self.write_to_file()

                else:
                    print('Invalid input!')
        except:
            print('Error!')

    def delete_user(self):
        try:
            self.open_file()
            f_name=input('Enter the name to delete-')
            if(f_name.isalpha()):
                for i in range(len(self.data['add_data'])):
                    if(self.data['add_data'][i]['f_name']==f_name):
                        print(self.data['add_data'][i])
                        del self.data['add_data'][i]
                        print('User Deleted!')
                        break
                self.write_to_file()
        except:
            print('Error!')

    def print_book(self):
        self.open_file()
        print(self.data)

    def sort_by_pincode(self):
        self.open_file()
        for i in range(len(self.data['add_data'])):
            for j in range(i+1,len(self.data['add_data'])):
                if(self.data['add_data'][i]['pincode']>self.data['add_data'][j]['pincode']):
                    self.data['add_data'][i],self.data['add_data'][j]=self.data['add_data'][j],self.data['add_data'][i]
        print(self.data)
        self.write_to_file()

    def sort_by_name(self):
        self.open_file()
        for i in range(len(self.data['add_data'])):
            for j in range(i+1,len(self.data['add_data'])):
                if (self.data['add_data'][i]['f_name']>self.data['add_data'][j]['f_name']):
                    (self.data['add_data'][i],self.data['add_data'][j])=(self.data['add_data'][j],self.data['add_data'][i])
        print(self.data)
        self.write_to_file()