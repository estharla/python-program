# class arithmetic:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def my_add(self):
#         print(self.a+self.b)
#     def my_sub(self):
#         print(self.a-self.b)
#     def my_mul(self):
#        print(self.a*self.b)
#     def my_div(self):
#        print(self.a/ self.b)

# a = arithmetic(10,20)
# a.my_add()
# a = arithmetic(30,20)
# a.my_sub()
# a = arithmetic(40,20)
# a.my_mul()


# my_amount=60000
# class city:
#     def __init__(self,amount):
#         self.amount = amount
#     def withdraw(self):
#         global my_amount
#         my_amount-=self.amount
#         print(my_amount)
#     def deposit(self):
#         global my_amount
#         my_amount+=self.amount
#         print(my_amount)
#     def house_loan(self):
#         if self.amount>=10000:
#             print("elgible for houseloan")
#         else:
#             print("not elgible for houseloan")
# class village(city):
#     def __init__(self,amount):
#         super().__init__(amount)
#     def crop_loan(self):
#         if self.amount>=20000:
#             print("elgible for croploan")
#         else:
#            print("not elgible for croploan") 
#     def cow_loan(self):
#         if self.amount>=30000:
#            print("elgible for cowloan")
#         else:
#             print("not elgible for cowloan")


# data = village(2000)
# data.withdraw()



# class resturant:
#     def __init__(self,fruits,tiffin,meals,biriyani):
#         self.fruits=fruits
#         self.tiffin=tiffin
#         self.meals=meals
#         self.biriyani=biriyani
#     def veg(self):
#         print("she eat the ap meals")
#     def nonveg(self):
#         print("she eat the banglore biriyani")
#     def patient(self):
#         print("she can not the banana")
#     def tiffin(self):
#         print("i eat the parota")

# x=resturant('fruits','tiffin','meals','biriyani')
# x.patient()
# x.nonveg()
# x.veg()



# class Tangutur:
#     def __init__(self, fish):
#         self.fish = fish

#     def fishcurry(self):
#         print(f"I can make fish curry with {self.fish}")


# class Kandhukur(Tangutur):
#     def __init__(self, fish, chicken):
#         super().__init__(fish)
#         self.chicken = chicken

#     def chickenfry(self):
#         print(f"I can make chicken fry with {self.chicken}")


# class Jarugumalli(Kandhukur):
#     def __init__(self, fish, chicken, panner):
#         super().__init__(fish, chicken)
#         self.panner = panner

#     def vegpanner(self):
#         print(f"I can make veg panner with {self.panner}")



# x = Jarugumalli("Salmon", "Broiler Chicken", "Paneer")
# x.fishcurry()
# x.chickenfry()
# x.vegpanner()


# class Breakfast:
#     def cooking(self):
#         print("I am making breakfast")

# class Lunch(Breakfast):
#     def cooking(self):
#         print("I am making lunch")

# class Dinner(Lunch):
#     def cooking(self):
#         print("I am making dinner")


# a = Breakfast()
# b = Lunch()
# c = Dinner()
# a.cooking()
# b.cooking()
# c.cooking()


# class payment:
#     def pay(self,amount):
#         pass
# class netbanking(payment):
#     def pay(self,amount):
#         print(f"i am doing the payment {amount}through netbanking")
# class debitcard(payment):
#     def pay(self,amount):
#         print(f"i am doing the payment {amount}through debitcard")
# class creditcard(payment):
#     def pay(self,amount):
#         print(f"i am doing the ")



# class Gpay:
#     def pay(self):
#         print("Paying amount using Gpay")

# class Phonepay:
#     def pay(self):
#         print("Paying amount using Phonepay")

# class Paytm:
#     def pay(self):
#         print("Paying amount using Paytm")

# def billing(x):
#     x.pay()

# billing(Gpay())
# billing(Phonepay())
# billing(Paytm()


# a=30
# b=40
# sum=a+b
# print(sum)

# a=10
# b=40
# a=("first number")
# b=("second number")
# print(a+b)


# a=40
# b=60
# print(max(a,b))


# a=6
# b=8
# if a > b:
#     print(a)
# else:
#     print(b)


# def is_perfect_sq(x):
#     s = int(math.sqrt(x))
#     return s * s == x

# def is_fibonacci(n):
#     return is_perfect_sq(5 * n * n + 4) or is_perfect_sq(5 * n * n - 4)

# for i in range(1, 7):
#     if is_fibonacci(i):
#         print(f"{i} is a Fibonacci Number")
#     else:
#         print(f"{i} is not a Fibonacci Number")




#  import math

#  def is_perfect_sq(x):
#      s = int(math.sqrt(x))
#      return s * s == x
#  def is_fibonacci(n):
#     return is_perfect_sq(5 * n * n + 4) or is_perfect_sq(5 * n * n - 4) 
# for i in range(1, 7):
#      if is_fibonacci(i):
#          print(f"{i} is a Fibonacci Number")
#      else:
#          print(f"{i} is not a Fibonacci Number")


# import math

# def is_perfect_sq(x):
#     s = int(math.sqrt(x))
#     return s * s == x

# def is_fibonacci(n):   
#     return is_perfect_sq(5 * n * n + 4) or is_perfect_sq(5 * n * n - 4)

# for i in range(1, 7):
#     if is_fibonacci(i):
#         print(f"{i} is a Fibonacci Number")
#     else:
#         print(f"{i} is not a Fibonacci Number")



# res = lambda a,b: a+b
# print (res (20,6))



# def my_si(p, t, r):
#     return (p * t * r) / 100

# p = 5
# t = 7
# r = 9

# res = my_si(p, t, r)
# print("Simple Interest =", res)



# my_si = lambda p, t, r: (p * t * r) / 100

# print(my_si(20, 10, 30))

# def my_ci(p, t, r):
#     a = p * (1 + r/100) ** t
#     return a - p

# print(my_ci(30, 20, 60))


# x=lambda p,t,r:(p(1+(r/100)))**t
# print(x(10000,12,2))


# def my_ci(p, t, r):
#     a = p * (1 + r/100) ** t
# x=my_ci(1000,12,2)
# print(x)


# a=int(input("enter your number"))
# if a>1:
#     for i in range(2,a):
#         if a%2==0:
#             print("this is not prime number")
#             break
#     else:
#         print("this is a prime number")


# x=int(input("enter your first number"))
# y=int(input("enter your second number"))
# for a in range(x,y+1):
#     if a>1:
#         for i in range(2,a):
#             if a%2==0:
#                 break
#         else:
#             print(a)


# a=[1,5,50,500,22,-3]
# sum=0
# for i in a:
#     sum=sum+(i**2)

# a = [1, 5, 50, 500, 22, -3]
# sum = 0

# for i in a:
#     sum = sum + (i ** 2)

# print(sum)


# n=int(input("enter uoyr number"))
# sum=0
# for i in range(1,n+1):
#     sum = sum(i**2)
# print(sum)


# n = int(input("Enter your number: "))
# sum = 0

# for i in range(1, n + 1):
#     sum = sum + (i ** 2)

# print(sum)


# a=[1,5,50,500,22,-3]
# b=[]
# for i in a:
#     b.append(i**2)
# print(b)



# a=[30,40,60,1000,-4]
# b=[]
# for i in a:
#     b.append(i**2)
# print(b)



# def my_square_list(a):
#     b = []
#     for i in a:
#         b.append(i**2)
#     return b

# a = [10, 30, 40, 400, 8]
# result = my_square_list(a)
# print(result) 



# def my_square_list(a):
#     b=[]
#     for i in a:
#         b.append(i**2)
#     return b
# a=[30,20,4,8,300]
# result = my_square_list(a)
# print(result)



# n=int(input("enter your number"))
# a=0
# b=1
# if n==1:
#     print(a)
# elif n==2
#     print(b)
# else:
#     for i in range(3,3)
#     c=a+b
#     a=b
#     b=c
#     print(b)



# n = int(input("Enter your number: "))

# a = 0
# b = 1

# if n == 1:
#     print(a)

# elif n == 2:
#     print(a)
#     print(b)

# else:
#     print(a)
#     print(b)
#     for i in range(3, n+1):
#         c = a + b
#         print(c)
#         a = b
#         b = c



# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))

# s = (a + b + c) / 2 

# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# print("Area of the triangle =", area)



# a = 6
# b = 8

# print("before swap:", a, b)

# b, a = a, b

# print("after swap:", a, b)




# import random as vyshu
# a= vyshu. randint(0,8)
# print(a)



# a=int(input("enter a side a:"))
# b=int(input("enter a side b:"))
# c=int(input("enter a side c:"))
# s=(a+b+c)/2
# area=s*(s-a)*(s-b)*(s-c)
# print("area of triangle =", area)



# km = float(input("Enter distance in kilometers: "))

# miles = km * 0.621371

# print("Distance in miles:", miles)


# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit:", fahrenheit)




# num = float(input("Enter a number: "))

# if num > 0:
#     print("The number is Positive")
# elif num < 0:
#     print("The number is Negative")
# else:
#     print("The number is Zero")





# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is Odd")





# num = float(input("Enter a number: "))

# if num > 0:
#     print("The number is Positive")
# elif num < 0:
#     print("The number is Negative")
# else:
#     print("The number is Zero")



# a=int(input("enter your number"))
# if a %2==0:
#     print("this is the even")
# else:
#     print("this is the odd")



























































        