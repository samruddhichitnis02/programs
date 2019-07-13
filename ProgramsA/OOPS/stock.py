import json
class Stock_Portfolio:
    def stock(self,data):
        for i in range(4):
            z=data["Stocks"][i]["Stock Name"] #takes the value of key Stocks Name
            a=data["Stocks"][i]["Share Price per stock"] #takes the value of key Share Price per stock
            print("The value of price per stock of",z, "is",a) #Prints the share price of per stock of each company
        print()

    def stock_calculation(self,data):
        count=0
        for i in range(4):
            p=data["Stocks"][i]["Stock Name"]
            b=data["Stocks"][i]["Share Price per stock"]
            c=data["Stocks"][i]["Number of Shares"]
            d=b*c    #from here we get the total stock price of each company
            count=count+d   #This gives the total price of the stock
            print("The total value of stocks of",p, "is-",d)
        print()
        print('The total stock is-',count)

S=Stock_Portfolio()
try:
    with open('stock.json', 'r') as f:
        data = json.load(f)
    S.stock(data)
    S.stock_calculation(data)
    f.close()
except:
    print('File Not Found!')
