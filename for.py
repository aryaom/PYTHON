for x in range(10):
    print(x,end=' ')
limit=int(input("\nenter a limit:"))
sum=0
for i in range(1,limit+1):
    if i%2 != 0:
      sum+=1
print("odd sum="+str(sum))


