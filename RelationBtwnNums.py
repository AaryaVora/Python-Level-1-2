a = int(input("Please enter a number."))
b = int(input("Please enter a number."))
c = int(input("Please enter a number."))
if a > b and a > c:
    print(a ,"is the greatest number")
elif b > a and b> c:
    print(b ,"is the greatest number")
elif c > b and c > a:
    print(c ,"is the greatest number")
elif a == b:
    print ("Both first and second values are equal.")
elif b == c:
    print ("Both second and third values are equal.")
elif c == a:
    print ("Both first and third values are equal.")
else:
    print("Please enter numbers.")
