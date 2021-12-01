n1=input("enter an integer list(space separated):")
n=list(map(int,n1.split()))
n=[x for x in n if x%2!=0]
print("list after removing even numbers:",end='')
print(n)
