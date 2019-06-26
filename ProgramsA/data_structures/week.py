y=int(input('Enter the year-'))
m=int(input('Enter the month-'))
d=int(input('Enter the day-'))
a=[ ]
b=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
c=[31 29 31 30 31 30 31 31 30 31 30 31 ]
def cal(month,start_date):


y0 = y − (14 − m) // 12
x = y0 + y0//4 − y0/100 + y0//400
m0 = m + 12 × ((14 − m) // 12) − 2
d0 = (d + x + 31m0 // 12) % 7

