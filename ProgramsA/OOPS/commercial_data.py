import json
import os

class Customer:
    def __init__(self):
        self.data=' '
        self.stock=[ ]


    def create(self):
        x={"Customer":[ ]}
        with open('customer.json','w') as f:
            json.dump(x,f,indent=2)
        f.close()

    def open_file(self):
        with open('customer.json', 'r') as f:
            self.data = json.load(f)
        f.close()

    def write_to_file(self):
        with open('customer.json','w') as f:
            json.dump(self.data,f,indent=2)
        f.close( )

    def menu(self):
        try:
            choice = int(input('Enter 1 to register 2  to main menu 3 to quit'))
            if (choice == 1):
                self.customer()
            elif(choice==2):
                self.menu()
            elif (choice == 3):
                return
            else:
                print('Invalid Choice!')
        except:
            print('Enter Integers!')
            self.menu()








    def customer(self):
        try:
            self.open_file()
            user = int(input('Enter the number of users-'))
            for i in range(user):
                name = input("Enter your name to register -")
                if(name.isalpha()):
                    y={ }
                    bal = int(input('Enter the amount with you-'))
                    y['name'] = name
                    y['bal'] = bal
                    y['stock'] = self.stock
                    st = 'y'
                    while (st == 'y'):
                        choice = int(input('Enter 1 to buy or 2 to sell-'))
                        with open('commercial.json', 'r') as fp:
                            data = json.load(fp)
                            fp.close()
                        if (choice == 1):
                            n1 = int(input('Enter the number of stock companies -'))
                            for i in range(n1):
                                z = {}
                                name1 = input(
                                    'Enter the stock name within these companies Facebook,Google,tcs,microsoft-')
                                share = int(input('Enter the number of shares-'))
                                z['name'] = name1
                                z['share'] = share
                                self.stock.append(z)
                                for i in range(0, len(data['Stocks'])):
                                    if (data['Stocks'][i]['Stock Name'] == name1):
                                        a = data["Stocks"][i]["Share Price per stock"]
                                        d = share * a
                                        bal = bal - d
                                        y['bal'] = bal
                                        print(y['bal'])
                                        bt = data["Stocks"][i]["Total Price"]
                                        bt = bt - d
                                        data["Stocks"][i]["Total Price"] = bt
                                        with open('commercial.json', 'w') as f:
                                            json.dump(data, f, indent=2)
                                        print('Your balance is-', y['bal'])



                        elif (choice == 2):
                            name2 = input('Enter the stock company you want to sell-')
                            share2 = int(input('Enter the number of share you invested-'))
                            for i in range(len(data['Stocks'])):
                                if (name2 == data['Stocks'][i]['Stock Name']):
                                    b = data['Stocks'][i]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][i]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][i]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                        f.close()

                                for j in range(len(self.stock)):
                                    if (self.stock[j]['name'] == name2):
                                        del self.stock[j]
                                        break

                        st = input('Enter y to continue-')
                        print(self.stock)
                    y['stock'] = self.stock
                    self.data["Customer"].append(y)
                    print(self.data)
                    self.write_to_file()
                else:
                    print('Error!')
                    self.customer()

        except:
            print('Invalid Input!')
            self.customer()


c=Customer()
c.menu()
