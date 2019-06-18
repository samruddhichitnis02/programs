import sys
class Payment():
	@staticmethod
	def monthly_pay(P,R,Y):
		n=12*Y
		r=R/(12*100)
		payment = (P*r)/(1-(1+r)**(-n))
		return payment



P=int(sys.argv[1])
Y=int(sys.argv[2])
R=int(sys.argv[3])

print('The payment is:',Payment.monthly_pay(P,R,Y))