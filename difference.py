color1=input("Enter a set of colors(space separated):")
color2=input("Enter a set of colors(space separated):")
c1=set(color1.split())
c2=set(color2.split())
print("The difference b/w",c1,"and",c2,"is",c1.difference(c2))

