list=input("enter a list:")
l1=map(int,list.split())
s=0
for i in l1:
    s+=i
print("the sum of all items in list",list,"is",s)
