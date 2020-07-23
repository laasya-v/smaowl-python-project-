a=int(input("first number"))
b=input("enter operation")
d=0.0
e=1
if b == "!":
    for i in range (1,a+1):
        e=e*i
    print(e)
else:
    c=float(input("second number"))
    
    
    if b == "+":
        d=a+c
        print(d)
    elif b == "-":
        d=a-c
        print(d)
    elif b == "*":
        d=a*c
        print(d)
    elif b == "/":
        d=a/c
        print(d)
    else:
        print ("not an available operation yet")
