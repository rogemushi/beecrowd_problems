a=1
b=2
c=3

def fibonot(n,a,b,c):
    
    if n < 0:
        print(b+n)
    else:

        a = b
        b = c
        c = a+b

        n = n - (c-b-1)
    fibonot(n + (c - b -1), a,b,c)

fibonot(int(input()),a,b,c)