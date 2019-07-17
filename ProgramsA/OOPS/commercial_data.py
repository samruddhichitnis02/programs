import json
class Customer:
    def __init__(self):
        self.data=' '
        self.y={ }
    def create(self):
        x={"Customer":[ ]}
        try:
            with open('customer.json','w') as f:
                json.dump(x,f,indent=2)
            f.close()
        except:
            print('File not found!')

    def open_file(self):
        with open('customer.json','r') as f:
            self.data=json.load(f)
        f.close()

    def write_to_file(self):
        with open('customer.json','w') as f:
            json.dump(self.data,f,indent=2)
        f.close()

    def register(self):
        self.open_file()
        try:
            name=input('Enter your name to register-')
            if(name.isalpha()):
                self.y['name']=name
                bal=int(input('Enter ypur balance amount-'))
                self.y['bal']=bal
                self.y['stock']=[ ]
                self.data['Customer'].append(self.y)
                self.write_to_file()
            else:
                print('Enter a Valid Name to register-')
        except:
            print('Invalid Input!')

    def login(self):
        self.open_file()
        try:
            name=input('Enter your name to login-')
            if(name.isalpha):
                for i in range(len(self.data['Customer'])):
                    if(name==self.data['Customer'][i]['name']):
                        print('Enter 1 to buy')
                        print('2 to sell')
                        print('3 to exit')
                        choice=int(input())
                        if(choice==1):
                            self.buy(name)
                        elif(choice==2):
                            self.sell(name)
                        elif(choice==3):
                            pass
                        else:
                            print('Invalid Input!')
            else:
                print('Type a Valid Name!')
        except:
            print('Invalid Input!')

    def buy(self,name):
        self.open_file()
        try:
            with open('commercial.json','r') as f:
                data=json.load(f)
                for i in range(len(data['Stocks'])):
                    name2=data['Stocks'][i]['Stock Name']
                    Price=data['Stocks'][i]['Share Price per stock']
                    print('Name-',name2)
                    print('Price Per Stock-',Price)
            f.close()
            for i in range(len(self.data['Customer'])):
                if (name == self.data['Customer'][i]['name']):
                    amt = self.data['Customer'][i]['bal']
                    name1 = input('Enter the Company you want to buy shares of-')
                    if (name == self.data['Customer'][i]['name']):
                        z = {}
                        if (name1.isalpha()):
                            z['name'] = name1
                            shares = int(input('Enter the number of shares from that Company-'))
                            z['Shares'] = shares
                            for j in range(len(data['Stocks'])):
                                if(name1==data['Stocks'][j]['Stock Name']):
                                    price = data['Stocks'][j]['Share Price per stock']
                                    amount = amt - (shares * price)
                                    sh = data['Stocks'][j]['Number of Shares']
                                    b= sh - shares
                                    print(b)
                                    data['Stocks'][j]['Number of Shares'] = b
                                    self.data['Customer'][i]['bal'] = amount
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                        f.close()
                            self.data['Customer'][i]['stock'].append(z)
            self.write_to_file()


        except:
            print('Invalid Input!')

    def sell(self,name):
        self.open_file()
        try:
            with open('commercial.json','r') as f:
                data=json.load(f)
            f.close()
            for i in range(len(self.data['Customer'])):
                if (name == self.data['Customer'][i]['name']):
                    print(self.data['Customer'][i]['stock'])
                    name1=input('Enter the company you want to delete-')
                    share=int(input('Enter the shares you invested-'))
                    amt=self.data['Customer'][i]['bal']
                    for j in range(len(self.data['Customer'][i]['stock'])):
                        if(name1==self.data['Customer'][i]['stock'][j]['name'] and share==self.data['Customer'][i]['stock'][j]['Shares']):
                            del self.data['Customer'][i]['stock'][j]['name']
                            del self.data['Customer'][i]['stock'][j]['Shares']
                        for j in range(len(data['Stocks'])):
                            if (name1 == data['Stocks'][j]['Stock Name']):
                                price = data['Stocks'][j]['Share Price per stock']
                                amount = amt + (share * price)
                                sh = data['Stocks'][j]['Number of Shares']
                                b = sh + share
                                print(b)
                                data['Stocks'][j]['Number of Shares'] = b
                                self.data['Customer'][i]['bal'] = amount
                                with open('commercial.json', 'w') as f:
                                    json.dump(data, f, indent=2)
                                    f.close()
            self.write_to_file()
        except:
            print('Invalid Input!')
