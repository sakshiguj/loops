a={}
b=0
while b<5:
   name=input("Enter your name: ")
   mark=int(input("enter the marks:"))
   if name not in a:
       a[name]=mark
       b=b+1
print(a)

# f={}
# for i in range(1,5):
#     a=input("enter key")
#     b=input("enter value")
#     f.update({a:b})
# print(f)