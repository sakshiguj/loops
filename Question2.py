dict1={'name':'Raju', 'marks':56}
for i in dict1.keys():
    s=input('enter your key name:  ')
    if s in dict1:
        print("Exist")
    else:
        print("Not exist")

