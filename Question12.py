n=int(input("enter the number"))
# n=10
# d={i:i ** 2 for i in range(1,n+1)}
# print(d)

d={}
for i in range(1,n+1):
    d[i]=i**2
print(d)