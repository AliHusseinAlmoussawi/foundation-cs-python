


## Exercise 1:
top=float(input("Top:"))
bottom=float(input("Bottom:"))
val=float(input("value:"))
print(val>bottom and val<top)

## Exercise 2:
a=int(input("fisrt number:"))
b=int(input("second number:"))
c=int(input("third number:"))
max=b
min=b
if a>b:
    if a>c:
        max=a
    else:
        max=c
if a<b:
    if a<c:
        min=a
    else:
        min=c
print("Max:",max)
print("Min:",min)

## Exercise 3:
grade=int(input("Total grade:"))
if grade>89 and grade<=100:
    print("A")
elif grade>79 and grade<=100:
    print("B")
elif grade>69 and grade<=100:
    print("C")
elif grade>59 and grade<=100:
    print("D")
elif grade<=59 and grade>=0:
    print("F")
else:
    print("Wrong input")

