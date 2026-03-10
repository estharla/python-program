# a=['mango','banana','oange','apple',];
# b=[i for i in a if 'm' in i];
# for i in a:
#     if 'm' in i:
#      b.append(i)
# print(b) 




def my_add(*a):
    print("my number is:", a[0])
    print("my fav number is:", a[2])
    print("my fav num sum is:", a[0] + a[2])

my_add(20, 30, 40, 50)