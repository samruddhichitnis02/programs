import sys
class Util():
    @staticmethod
    def Day_of_week(d,m,y):
        y0= y - (14-m) // 12
        x= y0 + y0 //4 - y0 //100 + y0 // 400
        m0 = m + 12 * ((14-m) // 12) - 2
        d0 = (d + x + 31*m0 // 12)%7
        if(d0==0):
            print('Sunday')
        elif(d0==1):
            print('Monday')
        elif (d0 == 2):
            print('Tuesday')
        elif (d0 == 3):
            print('Wednesday')
        elif (d0 == 4):
            print('Thursday')
        elif (d0 == 5):
            print('Friday')
        else:
            print('Saturday')

d=int(sys.argv[1])
m=int(sys.argv[2])
y=int(sys.argv[3])
Util.Day_of_week(d,m,y)