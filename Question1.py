dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# dic1[2]=60
# print(dic1)
for key in dic1:
    if key in dic2:
        dic1[key]=dic1[key]+dic2[key]
        dic2.update(dic3)
    else:
        dic2[key]=dic1[key]
print(dic2)            

# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 


