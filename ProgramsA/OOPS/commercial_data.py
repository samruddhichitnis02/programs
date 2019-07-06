import json
import os

def customer():
    with open('customer.json', 'a') as f:
        if (os.stat('customer.json').st_size > 0):
            user = int(input('Enter the number of users-'))
            for i in range(user):
                y = {}
                name = input("Enter your name to register -")
                bal = int(input('Enter the amount with you-'))
                y['name'] = name
                y['bal'] = bal
                stock = []
                y['stock'] = stock
                st = 'y'
                while (st == 'y'):
                    choice = int(input('Enter 1 to buy or 2 to sell-'))
                    if (choice == 1):
                        n1 = int(input('Enter the number of stock companies -'))
                        for i in range(n1):
                            z = {}
                            name1 = input('Enter the stock name within these companies Facebook,Google,tcs,microsoft-')
                            share = int(input('Enter the number of shares-'))
                            z['name'] = name1
                            z['share'] = share
                            stock.append(z)

                            with open('commercial.json', 'r') as fp:
                                data = json.load(fp)
                                if (name1 == 'facebook'):
                                    a = data["Stocks"][0]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    bt = data["Stocks"][0]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][0]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                                elif (name1 == 'google'):
                                    a = data["Stocks"][1]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    bt = data["Stocks"][1]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][1]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                                elif (name1 == 'tcs'):
                                    a = data["Stocks"][2]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    print(y['bal'])
                                    bt = data["Stocks"][2]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][2]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                                elif (name1 == 'microsoft'):
                                    a = data["Stocks"][3]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    bt = data["Stocks"][3]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][3]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                    elif (choice == 2):
                        name2 = input('Enter the stock company you want to sell-')
                        share2 = int(input('Enter the number of share you invested-'))
                        if (name2 == 'facebook'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'facebook'):
                                    b = data['Stocks'][0]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][0]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][0]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    del stock[i]
                                    break
                        elif (name2 == 'google'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'google'):
                                    b = data['Stocks'][1]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][1]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][1]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, inedent=2)
                                    del stock[i]
                                    break
                        elif (name2 == 'tcs'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'tcs'):
                                    b = data['Stocks'][2]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][2]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][2]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    del stock[i]
                                    break
                        elif (name2 == 'microsoft'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'microsoft'):
                                    b = data['Stocks'][3]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][3]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][3]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    del stock[i]
                                    break

                    st = input('Enter y to continue-')
                    print(stock)
                y['stock'] = stock
                x["Customer"].append(y)
        else:
            x = {"Customer": []}
            user = int(input('Enter the number of users-'))
            for i in range(user):
                y = {}
                name = input("Enter your name to register -")
                bal = int(input('Enter the amount with you-'))
                y['name'] = name
                y['bal'] = bal
                stock = []
                y['stock'] = stock
                st = 'y'
                while (st == 'y'):
                    choice = int(input('Enter 1 to buy or 2 to sell-'))
                    if (choice == 1):
                        n1 = int(input('Enter the number of stock companies -'))
                        for i in range(n1):
                            z = {}
                            name1 = input('Enter the stock name within these companies Facebook,Google,tcs,microsoft-')
                            share = int(input('Enter the number of shares-'))
                            z['name'] = name1
                            z['share'] = share
                            stock.append(z)

                            with open('commercial.json', 'r') as fp:
                                data = json.load(fp)
                                if (name1 == 'facebook'):
                                    a = data["Stocks"][0]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    bt = data["Stocks"][0]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][0]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                                elif (name1 == 'google'):
                                    a = data["Stocks"][1]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    bt = data["Stocks"][1]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][1]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                                elif (name1 == 'tcs'):
                                    a = data["Stocks"][2]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    print(y['bal'])
                                    bt = data["Stocks"][2]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][2]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                                elif (name1 == 'microsoft'):
                                    a = data["Stocks"][3]["Share Price per stock"]
                                    d = share * a
                                    bal = bal - d
                                    y['bal'] = bal
                                    bt = data["Stocks"][3]["Total Price"]
                                    bt = bt - d
                                    data["Stocks"][3]["Total Price"] = bt
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    print('Your balance is-', y['bal'])

                    elif (choice == 2):
                        name2 = input('Enter the stock company you want to sell-')
                        share2 = int(input('Enter the number of share you invested-'))
                        if (name2 == 'facebook'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'facebook'):
                                    b = data['Stocks'][0]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][0]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][0]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    del stock[i]
                                    break
                        elif (name2 == 'google'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'google'):
                                    b = data['Stocks'][1]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][1]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][1]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, inedent=2)
                                    del stock[i]
                                    break
                        elif (name2 == 'tcs'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'tcs'):
                                    b = data['Stocks'][2]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][2]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][2]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    del stock[i]
                                    break
                        elif (name2 == 'microsoft'):
                            for i in range(len(stock)):
                                if (stock[i]['name'] == 'microsoft'):
                                    b = data['Stocks'][3]["Share Price per stock"]
                                    q = share2 * b
                                    bal = bal + q
                                    y['bal'] = bal
                                    tb = data["Stocks"][3]["Total Price"]
                                    tb = tb - d
                                    data["Stocks"][3]["Total Price"] = tb
                                    with open('commercial.json', 'w') as f:
                                        json.dump(data, f, indent=2)
                                    del stock[i]
                                    break

                    st = input('Enter y to continue-')
                    print(stock)
                y['stock'] = stock
                x["Customer"].append(y)
                print(x)

customer()