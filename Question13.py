a={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50
}
h={}
# for i in a:
#     c=a[i]
#     for i in a:
#         b=a[i]
#         if c>b:
#             h[i]=b
# print(h)
for i in a:
    c=a[i]
    for i in a:
        b=a[i]
        if c<b:
            h[i]=b
print(h)


# h={}
# for i in a.keys():
#     h.update(a)
# print(h)