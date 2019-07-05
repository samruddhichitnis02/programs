import json

def customer():
    x = {"Customer": [ ]}
    user = int(input('Enter the number of users-'))
    for i in range(user):
        y={}
        name = input("Enter your name to register-")
        bal = int(input('Enter the amount with you-'))
        y['name']=name
        y['bal']=bal
        y['stock']=[ ]
        n1=int(input('Enter the number of stock companies-'))
        for i in range(n1):
            z={ }
            name1=input('Enter the stock name-')
            share=int(input('Enter the number of shares-'))
            z['name']=name1
            z['share']=share
            y['stock'].append(z)
            with open('commercial.json', 'r') as fp:
                data = json.load(fp)
            if(name1=='facebook'):
                a = data["Stocks"][0]["Share Price per stock"]
                d=share*a
                bal=bal-d
                y['bal']=bal
            elif (name1 == 'google'):
                a = data["Stocks"][1]["Share Price per stock"]
                d = share * a
                bal = bal - d
                y['bal'] = bal
            elif (name1 == 'tcs'):
                a = data["Stocks"][2]["Share Price per stock"]
                d = share * a
                bal = bal - d
                y['bal'] = bal
            elif (name1 == 'microsoft'):
                a = data["Stocks"][3]["Share Price per stock"]
                d = share * a
                bal = bal - d
                y['bal'] = bal

        x["Customer"].append(y)
        print(x)

    b=input('Enter the stock name to sell-')
    if(b=='tcs'):
        if y['stock']['name'] == 'tcs':
            del y['stock']['name']
    x["Customer"].append(y)
    print(x)



customer()