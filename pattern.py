a = 7
b = int(input("When to stop?"))
print(a,end=",")
for i in range (0,b-2):
    a = a + 3
    print(a,end=",")
    a = a - 2
    print(a,end=",")
print("......")
