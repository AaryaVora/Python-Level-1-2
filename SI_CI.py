principle_amount = int(input("Please enter the priniple amount : "))
rate = int(input("Please enter the rate of interest: "))
time = int(input("Please enter the time period: "))
si_ci = int(input("Enter 1 for simple interest and 2 for compound interest: "))
if si_ci == 1:
    si = principle_amount * rate * time / 100
    print("Simple interest = ",si )
elif si_ci == 2:
    ci = principle_amount * (1 + rate/100) ** time
    print ("Compound interest =",ci)