s1=input("enter the first string:")
s2=input("enter the second string:")
new_a=s2[:1]+s1[1:]
new_b=s1[:1]+s2[1:]
print("the new string after swapping first 2 chracters of both string:",(new_a+''+new_b))
