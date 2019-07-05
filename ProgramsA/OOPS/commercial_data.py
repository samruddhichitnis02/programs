import json

def Customer():
    name=input("Enter you name to register-")
    bal=int(input("Enter the amount you have-"))
    x = {"Customer": []}
    st='y'
    while(st=='y'):
        user=int(input('Enter the number of users-'))
        for i in range(user):
            choice=int(input('Enter 1 to buy 2 to sell 3 to print the report-'))
            if(choice==1):
                y={ }
                y['name']=name
                n=int(input('Enter the number of Stock companies-'))
                y['Stock_Name']=[ ]
                y['Number of Shares']=[ ]
                for i in range(n):
                    z=input('Enter the Company Name-')
                    y['Stock_Name'].append(z)
                    p=int(input('Enter the no of shares-'))
                    y['Number of Shares'].append(p)
                    with open('commercial.json', 'r') as fp:
                        data = json.load(fp)
                        if(z=="tcs"):
                            a=data["Stocks"][2]["Share Price per stock"]
                            d=p*a
                            bal=bal-d
                            print(bal)

                        elif (z == "google"):
                            a = data["Stocks"][1]["Share Price per stock"]
                            d = p * a
                            bal = bal - d
                            print(bal)

                        elif (z == "facebook"):
                            a = data["Stocks"][0]["Share Price per stock"]
                            d = p * a
                            bal = bal - d
                            print(bal)

                        elif (z == "microsoft"):
                            a = data["Stocks"][3]["Share Price per stock"]
                            d = p * a
                            bal = bal - d
                            print(bal)

                x["Customer"].append(y)
                print(x)
                with open('customer.json', 'w') as fp:  # write the dict to the json file
                    json.dump(x, fp)

            elif(choice==2):
                print(x)
                comp = input('Enter the Stock name you want to sell-')
                ab=int(input('Enter the no of shares you invested-'))
                if (comp == "tcs"):
                    k = data["Stocks"][2]["Share Price per stock"]
                    y["Stock_Name"].remove("tcs")
                    y["Number of Shares"].remove(ab)
                    j=k*ab
                    bal=bal+j
                    print(bal)
                elif (comp == "google"):
                    k = data["Stocks"][1]["Share Price per stock"]
                    y["Stock_Name"].remove("google")
                    y["Number of Shares"].remove(ab)
                    j=k*ab
                    bal=bal+j
                    print(bal)
                elif (comp == "facebook"):
                    k = data["Stocks"][0]["Share Price per stock"]
                    y["Stock_Name"].remove("facebook")
                    y["Number of Shares"].remove(ab)
                    j=k*ab
                    bal=bal+j
                    print(bal)
                elif (comp == "microsoft"):
                    k = data["Stocks"][3]["Share Price per stock"]
                    y["Stock_Name"].remove("microsoft")
                    y["Number of Shares"].remove(ab)
                    j=k*ab
                    bal=bal+j
                    print(bal)

                x["Customer"].clear()
                x["Customer"].append(y)
                with open('customer.json', 'w') as fp:
                    json.dump(x,fp)
                print(x)

            st = input('Enter y to continue or any other key to discontinue-')
Customer()
