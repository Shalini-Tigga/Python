a = int(input(""))
b = len(str(a))
c = 0
d = a
e = 1
while(b+1>1):
    c=d%(10**b)
    f = c //10**(b-1)
    b =  b - 1
    
    print(f)
