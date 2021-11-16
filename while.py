number=int(input('enter number:'))
s=0
while number > 0:
    s += number%10
    number=number//10
print(s)
