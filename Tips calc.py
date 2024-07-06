print("Welcome to the Tip Calculator")
bill=int(input("What was the total bill? $"))
tip=int(input("How much would you like tip?,10,12 or 15:150 "))
n=int(input("how many people should split the bill?"))
tbill=bill +(bill *(tip/100))

total=tbill/5
print(f"each person should pay {round(total,2)}")

