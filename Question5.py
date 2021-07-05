a=["one","two","three","four","five"]
b=[1,2,3,4,5,] 
# list1_list2=dict(zip(a,b))
# print(dict(list1_list2))



f=0
d={}
for i in a:
    d[i]=b[f]
    f+=1
print(d)

