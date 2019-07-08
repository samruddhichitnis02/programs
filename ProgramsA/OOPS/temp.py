import json
class Customer():
    def __init__(self):
        self.data=' '
        self.stock=[ ]

    def create(self):
        x={"Customer":[ ]}
        with open('customer.json','w') as f:
            json.dump(x,f,indent=2)
        f.close()



    def open_file(self):
        with open('customer.json','r') as f:
            self.data=json.load(f)
        f.close( )

    def write_to_file(self):
        with open('customer.json','w') as f:
            json.dump(self.data,f, indent=2)
        f.close( )

    def customer_add(self):
        self.open_file()
        y={ }
        try:
            name=input('Enter your name-')
            bal=int(input('Enter the balance-'))
            y['name']=name
            y['bal']=bal
            y['stock']=[ ]

            if(name.isalpha()):
                self.data['Customer'].append(y)
                self.write_to_file()
            else:
                print('Invalid Input!')
        except:
            print('Invalid Input!')
            self.customer_add()

    def buy_shares(self):
        self.open_file()
        try:
            name=input('Enter the account name-')
            if(data['Customer']y['name']==name):
                n=int(input('Enter the number of companies-'))
                for i in range(n):
                    z={ }
                    name1=input('Enter the name of companies- ')
                    share=int(input('Enter the number of shares-'))
                    z['name']=name1
                    z['share']=share
                    self.stock.append(z)





C=Customer()
