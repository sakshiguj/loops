a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
h=[]
b={}
for i in a:
     for j in i:
          if i not in h:
              h.append(i)
print(h)