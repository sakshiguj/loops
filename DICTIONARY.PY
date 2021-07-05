 
# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population)) 


 
# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result) 


# fruit = {'mango': 40, 'banana': 10, 'cherry': 20}
# print(fruit)


# mydict = {'x':[1,2,3,4], 'y':"Hello World", 'z':4.0}
# print(mydict)



# declaring an empty dictionary
# fruit = {}
# # adding key-value pairs to dictionary
# fruit['mango'] = 40
# fruit['banana'] = 10
# fruit['cherry'] = 20

# print(fruit)



# fruit = {'mango':40, 'banana':10, 'cherry':20}
# print(list(fruit.keys()))
# print(list(fruit.values()))


# # declaring an empty dictionary
# fruit = {}

# # adding key-value pairs to dictionary
# fruit['mango'] = 40
# fruit['banana'] = 10
# fruit['cherry'] = 20

# print(fruit)


# fruit = {'mango':40, 'banana':10, 'cherry':20}
# print(list(fruit.keys()))
# print(list(fruit.values()))


 
# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }

# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic) 


a={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
h={}
for i in a:
    c=a[i]
    for i in a:
        b=a[i]
        if c>b:
            h[i]=b
for i in a:
    c=a[i]
    for i in a:
        b=a[i]
        if c<b:
            h[i]=b
print(h)
