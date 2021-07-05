# s={1:1,2:4,3:9,4:16,5:25}
# print(s)
# s.clear()
# print(s)

# print(s.items())

# print(s.popitem())
# print(s)


# print(s.keys())

# print(s.values())



# markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist=list(markdict.items())
# print(marklist)


# mylist=[5,3,7,8,20,15,2,6,10,1]
# for i in mylist:
#     if (i%2==0):
#         mylist.remove(i)
# print (mylist)


# d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
# d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}

# for a,b in d2.items():
#     d1[a]=b

# print(d1)



# d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
# d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}
# for i,j in d2.items():
#         d1[i]=j
# print(d1)



# d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
# d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}
# d1.update(d2)
# print(d1)


# fruit = {'mango':40, 'banana':10, 'cherry':20}
# print(list(fruit.keys()))
# print(list(fruit.values()))


# 40
# 10
# fruit = {'mango':40,'banana':10}
# print(fruit['mango'])
# print(fruit['banana'])



# fruit = {'mango':40,'banana':10}
# print(fruit.get('mango'))
# print(fruit.get('banana'))


# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# del mydict['age']  
# print(mydict)  




# mydict = {1: 1, 2: 8, 3: 27, 4: 64}
# print(2 in mydict)
# print(5 in mydict)
# print(4 not in mydict)



# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# for k in mydict:
#    print("key =", k)
#    print("value =", mydict[k])


# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# for k, v in mydict.items():
#     print("key =", k)
#     print("value =", v)


# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# for v in mydict.values():
#     print("value =", v)



dict1 = {'a': 20, 'b': 10, 'c': [1, 2, 3]}
dict2 = dict1.copy()
dict2['b'] = 30
dict2['c'] = [1, 2, 3, 4]
print("Original dictionary:", dict1)
print("New dictionary:", dict2)


# dict1 = {'a': 20, 'b': 10, 'c': [1, 2, 3]}
# dict2 = dict(dict1)
# dict2['b'] = 30
# dict2['c'] = [1, 2, 3, 4]
# print("Original dictionary:", dict1)
# print("New dictionary:", dict2)



# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# print(len(mydict))


# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# print(sorted(mydict))




# mydict = {2: 'John', 1: 45, 3: 'male'}
# print(sorted(mydict, reverse=True))


# a={1:"one",2:"two",3:"three"}
# x=a.copy()
# print(x)

