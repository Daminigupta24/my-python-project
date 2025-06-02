print("Welcome to python pizza deliveries")
size=input("what size pizza do you want? S, M or L:")
pepprani=input("do you want pepperoni Y or N:")
ex_cheese=input("do you want extra cheese : Y or N:")
bill=0
if size=='S':
    bill=15
elif size=='M':
    bill=20
elif size=='L':
    bill=25
if pepprani=='Y' and size=='S':
    bill=bill+2
else:
    bill=bill+3
if ex_cheese=='Y':
    bill=bill+1
print(f'the total bill is {bill}')
#logical opeartors, and or and not
