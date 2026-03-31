# print("hello ,I am archana solanki")

# #hii, i am archana.

# """buyiuiuinbnbj
# bjjgjhghbmnbnnmmb  vhhg ghhffytyt hfyuu
# jjhghhjhkklkljklk"""


# sherni = "archana"

# SherniArchana = "ARCHANA" #Pascalcase

# sherniArchana = "ARCHANA" #camelcase

# sherni_Archana = "ARCHANA" #snakecase
# print(SherniArchana)

# a = -12
# c = 12/3

# v = 34j #sirf j hi use kar sakte hai ,baki koi alphabet use karne pr Error dega.
# print(type(v))

# b = 'archana solanki'
# d = True

# print(type(d))

# e = "A"
# print(ord(e))

# f = 65
# print(chr(f))

# g = "Hello brother"
# print(g[7])
# print(g[0:3:1])
# print(g[6::1])

# f = str(f)
# print(type(f))

# #  There are total 7 values jo false degi in boolean which are as follows:
# #  false,0,0.0," ",[ ],( ),{ }

# print(12/4)# yeh always 3.0 float  ke form me dega because of explicit function

# name = "archana" #INPUT
# age = "21"#INPUT

# print(name,age) #OUTPUT

# print("hello my name is",name,"and my age is ",age) 
# print(f"my name is {name} and my age is {age}") #formatted string

# age = input("hello my age is :")
# print(age)

# m = 30
# n = 20
# print(m + n)
# print(m - n)
# print(m/n)
# print(m//n)

#print(5**100)
# print(32%5)


# print(12+4/2)#BODMAS RULE

#Assignment operator 

# a = 23

#compound assignment operator 

# a = 20
# a += 20 #o/p:40
# a += 40 # o/p: 40+40=80

# print(a)# output : 80

# if 5 < 2:
#   print("Five is greater than two!")

# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!") 


# x = 5
# y = "Hello, World!"

# print(x)
# print(y)

# print(123 > 100 and 34 ==34 and 45<90)# output: TRUE (WHEN WE USE AND IT MEANS ALL THE CONDITIONS SHOULD BE TRUE FOR GETTING ANSWER TRUE)
# print(123 > 350 and 35 == 35) # if one condition is false thenn whole statement gets false.
# #In AND Condition all the conditions should be true then only our OUTPUT will be TRUE


# # OR operation me koi ek condition bhi galat hoti hai then out whole statement goes FALSE.5
# # print(12 != 12 or 23 == 45 or  67 ==54 or 10>5)

# # print(126>130)
# # print((456 ==456) != (235 ==236))
# # print(12<10 or 45 == 56 or 69 > 70 or 15 != 13)#true
# # print(True and bool(0))

# # x, y, z = "Orange", "Banana", "Cherry"
# # print(x)
# # print(y)
# # print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)



#If.... else....

# a = 7

# if a > 10:
#     print("hello")

# else:
#     print("i will do task B")

# money = int(input("please provide me the money: "))

# if money == 10:
#     print("I will have a choco bar ice cream")

# elif money == 20:
#     print("I will have a mango dolly")

# else:
#     print("I will have a cone")

#1.Accept 2 numbers and print the greatest between them.
# num1 = int(input("please enter your first number:"))
# num2 = int(input("please enter your second number:"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")

# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
     
# else:
#      print("Bothe the numbers are same")


#2.Accept the gender from the user as char and print the respective greeting message.
#Ex. Good morning sir (pn the basis of gender)

# gen =  input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")

# elif gen == 'F'or gen == 'f':
#      print("Good morning ma'am")

# else:
#     print("Unidentified gender")

#3.Accept the integer and check whether it is an even number or odd.

# num = int(input("please tell your number:-"))
# if num%2 == 0:
#     print("Even number")

# else:
#     print("odd number")

#4.Accept name and age from the user.check if the user is a valid voter or not.
# Ex. "Hello shery you are the valid voter"

# name = input("please tell your name:-")
# age = int(input("tell your age:"))

# if age >=18:
#     print(f"hello {name} you are a valid voter")

# else:
#     print(f"hello {name} you are not a valid voter")

#5. Accept a year and check if it is a leap year or not 
#(leap year is a year which is divisible by 4)

# year = int(input("tell your year:-"))

# if year %100 == 0 and year %400 == 0:
#     print("its a leap year")

# elif year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")


#for loop
# a = range(1,21,1)

# # for i in a:
# #     print(i)

# for i in range(21):
#      print(i)

# for i in range(20,51):
#     print(i)

# for i in range(16,0,-1):
#     print(i)

#lets print a table of 5

# for i in range(7,71,7):
#     print(i)

# n = int(input("which table you want?"))

# for i in range(n,(n*10)+1,n):
#     print(i)

# a = "I am genius"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])
# for i in range(7):
#     print(a[i])

# a = "I am genius"

# for i in a:
#     print(i)

# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)

# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")

# que. Acceptt the integer and print hello world n times.

# n = int(input("please enter your number:"))

# for i in range(n):
#     print("hello world")

#que.print natural numbers upto n.

# n = int(input("please tell your number:"))

# for i in range(1,n+1):
#     print(i)

#que. reverse for loop.print n to 1.

# n = int(input("please enter your number:"))

# for i in range(n,0,-1):
#     print(i)

#que. take a number as input and print its table.
# n = int(input("which table you want:"))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# que. sum upto n terms.

# n = int(input("please enter your number:"))

# sum = 0

# for i in range(1,n+1):
#     sum = sum + i

# print(f"you sum is {sum}")

# n = int(input("please enter your number:"))

# fact = 1

# for i in range(1,n+1):
#     fact = fact * i

# print(f"your factorial is {fact}")

#que. print the sum of alll even and odd numbers in range seperatly.

# n = int(input("tell your number:-"))
# even = 0
# odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"your even and odd sum are {even} , {odd}")

#que.print all the factors of a number.

# n = int(input("please tell your number:"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

#que.accept a number and check if it a perferct number or not.A number whose sum of factors is equal to the number itself.
#ex.6 = 1,2,3 = 6
# n = int(input("check your number is perfect or not:-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         print(i)
#         sum = sum + i
# print(sum)

# if sum == n:
#     print("your number is perfect number")
# else:
#     print("your number is perfect number.")


#que. check wether the nuumber is prime or not.
# n = int(input("check your number is prime or not:-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# print(count)

# if count == 2:
#     print("your number is prime.")
# else:
#     print("your number is not prime")

#que. reverse a string without using in built function.

# First approach
# a =  "ARCHANA"
# print(a[::-1])

#second approach
# a =  "ARCHANA"
# b = ""

# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print(b)

#que. check the string is palindrome or not.
# a =  "naman"
# b = ""

# for i in range(len(a)-1,-1,-1):
#         b = b + a[i]

# if b == a:
#         print("Its a palindrome number")
# else:
#         print("its not a palindrome number")

#que. Count all letters,digits,and special symbols from a given string
#Given: str1 = "P@#yn26at^&i5ve"
#Expected outcome:Total counts of chars,digits,and symbols
#Chars = 8, Digits = 3,Symbol = 4



# a = "P@#yn26at^&i5ve"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1

# print(f"your digits are {dig}\n your alphabets are {char}\nyour special character are {spchr}")

#WHILE LOOP:while is work in certain coondition,agar condition nahi dege to woh infinite chalta jayega.

# a = 1

# while a<=30:
#     print(a)
#     a = a + 1

#que. Separate each digit of a number and print it on the new line.

# a = int(input("tell your number:"))

# while a > 0:
#     print(a%10)
#     a = a // 10

#que.Accept the number and print its reverse.

# a = int(input("tell your number:"))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)

#que. Accept the number and check if it is a palindromic number (if number and its reverse are equal)

# a = int(input("tell your number:"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if copy == rev:
#     print("palindromic number")
# else:
#     print("not a palindromic number")

#que. Create a random number guessing game with python.

# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#         guess = int(input("please enter your number:"))
#         if num == guess:
#                 tries +=1
#                 print("you guessed it right")
#                 break

#         elif num < guess:
#                 print("go a little lower")
#                 tries +=1

#         elif num > guess:
#                 print("go a little higher")
#                 tries +=1
#         else:
#                 tries +=1
#                 print("sorry you are wrong")

# FUNCTIONS.....

# def hello():
#     print("hello how are you?")
    
# hello()

# def sum(a,b):
#     print(f"The sum of numbers is {a + b}")

# sum(12,12)

# def add(a,b):
#     return a + b
# print(add(3,6))

# def introduce(name,age):
#     print(f"I am {name} and my age is {age}")

# introduce(name="archana", age=21)

# def greet(name="Guest"):
#     print(f"hello, {name}")

# greet()
# greet("Bob")

# def sum(a,b=45): #Default argument passed
#     print(f"The sum is {a+b}")

# sum(12,56)

#qye. checking a string is palindrome or not by using function.

# def palindrome(st):
#     rev = "" 
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f"{st} is a paindrome")
#     else:
#         print(f"{st} is not a palindrome")

# palindrome("naman")
# palindrome("cursor")

# LIST.....

# a = [12,13,14,15,3,56,19,4.5,True,print()]

# # first way using index
# for i in range(len(a)):
#     print(a[i])

#2nd way directly on values

# for i in a:
#     print(i)

#que.print positive and negative elements of a list.
# l = [-45,67,12,-68,-69,34]
# print("positive elements are:")
# for i in l:
#     if i>=0:
#         print(i)
# print("negative elements are:")
# for i in l:
#     if i<0:
#         print(i)

#mean of list elements
# l = [12,45,73,24,45,58]
# sum = 0

# for i in l:
#     sum = sum + i
# print(sum/len(l))

#find the greatest element and print its index too.
# l = [12,45,73,24,45,58]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")

#que.find the second largest number

# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest,largest)

#que.check if the list is sorted or not.

# a = [12,13,14,15]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")

#DICTIONARY

# d = {}

# print(type(d))

# d = {10:100,20:200,30:300,40:400}

# d2 = d.copy()

#write a python script to merge two python dictionaries.
# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d10)

#write a python program to sum all the values in a dictionary.
# d1 = {10:100,20:200,30:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

#count the freqeuncy of each elements in a list.

# a =  [1,1,1,2,2,2,2,2,3,3,3,3,3,3,5,5,5,6,7,9,9]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1

# print(d)
    





    




