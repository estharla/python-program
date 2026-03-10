#  import day5
#  import pandas
#  day5.my_avg(50,60,70)



#  import day5 as d5
#  d5.my_avg(50,60,70)



# def greet(name):
#     print("hello",name)
# greet("vyshu")



# import day5
# import pandas

# day5.my_avg(20, 30, 40)


# def add_numbers(a,b):
#     return a-b
# result =add_numbers(30,40)
# print(result)



#  a=('mango','banana','cherry')
#  b=iter(a)
#  print(next(b))
#  c=iter(b)




# import datetime
# a = datetime.datetime.now()
# print(a)





# import datetime

# a = datetime.datetime.now()

# print(a.year)
# print(a.strftime("%A"))




# import datetime

# a = datetime.datetime(2025,12,2)

# print(a.year)
# print(a.strftime("%A"))


# day = "Sunday"

# if day == "Sunday":
#     print("Sunday is holiday")
# else:
#     print("Working day")



# import datetime
# a = datetime.datetime(2020,7,15)
# b = a.strftime("%A")
# if b =='manday':
#   print('the working day')
# else:
#     print('the is holiday')



# import datetime

# a = datetime.datetime(2020, 7, 15)
# b = a.strftime("%A")

# if b == "Monday":
#     print("The working day")
# else:
#     print("It is holiday")



# import re
# x = ('my village name is kandukur')
# b =x.search('village',)
# if b:
#     print('it is available')
# else:
#     print('not available')




# try:
#     a=5
#     b=6
#     if a>=100:
#         print(a+b)
# except NameError:
#     print("this is NameError")
# else:
#     print("you have an Error")
# finally:
#     print("completed my task")



# try:
#     a=5
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("this Number by ZeroDivision Error")
# else:
#     print("yoy have some Error")
# finally:
#     print("this is completed")



# a="hi vyshnavi, you have to pay 2000rs"
# print(a)

# x='vyshu'
# y=2000
# a=f"hi {x},you have to pay {y}rs"
# print(a)

# x='vyshu'
# y=2000
# a="hi {},you have to pay{}".format(y,x)
# print(a)


class Canara:
    def __init__(self, x):
        self.x = x

    def deposit(self, amount):
        self.x = self.x + amount
        print("Balance after deposit:", self.x)

    def withdraw(self, amount):
        self.x = self.x - amount
        print("Balance after withdrawal:", self.x)









