# name={
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 

# s={}
# for i in name.items():
#     s.update(name)
# print(s)

a={}
n=int(input("enter the number:"))
for i in range(n):
    p=input("enter the keys:")
    q=input("enter the values:")
    a.update({p:q})
print(a,end="")
