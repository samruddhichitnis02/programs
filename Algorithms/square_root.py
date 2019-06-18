class Square():
    @staticmethod
    def Root(c):
        epsilon=1e-15
        t = c
        while(abs(t-c/t)>epsilon*t):
            t=(c/t+t)/2
        print('The square-root of the number is-',t)

c=int(input('Enter a number-'))
Square.Root(c)