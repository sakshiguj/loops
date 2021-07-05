c = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"] 
# c=input("enter the number")
d={}
for i in c:
    keys=d.keys()
    if i in keys:
        d[i]+=1
    else:
        d[i]=1
print(d)

# d=[]
# while i<len(c):
#     j=0
#     a=[]
#     count=0
#     while j<len(c):
#         if c[i]==c[j]:
#             count=count+1
#         j=j+1
#     a.append(c[i])
#     a.append(count)
#     if a not in d:
#         d.append(a)
#     i=i+1
# print(d)




# {M:1,I:4,S:4,P:2}