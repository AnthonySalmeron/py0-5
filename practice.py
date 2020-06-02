# birth_year=input("Birth Year: ")#everything typed here will count as string
# age = 2020-int(birth_year)
# print(type(birth_year))#<class 'str'>
# print(type(age))#<class 'int'>
# #int()
# #float()
# #bool()
# print(age)


# print(int(input("What is your weight(lbs): "))*0.45)#prints your weight in kg


# var = '''
# This,
#
# lets me write
#
# multiline letters
# '''
# print(var)


# coures = 'hihihi'
# # print(coures[-1])#i
# print(coures[0:3])#like slice, returns 0-3 except 3
# print(coures[1:])#from index 1 return rest of string
# print(coures[:3])#assumes 0 as the starting index
# #can use negative index for second one


# # formatted strings
# first="jonh"
# last ="smith"
# message = f'{first} [{last}] is a coder'#template literal
# print(message)


# # string methods
# hi= 'hi'
# print(len(hi))#general purpose function, works with lists
# print(hi.upper())#does not change original
# print(hi.find('i'))#indexof
# print(hi.replace('hi','bye'))#doesnt change original
# print('h' in hi)#boolean
# print(hi.title())#capitalizes first char


# import math #math module
# math operators same as in js
# x=3
# x+=3
# x-=2
# x=10+3*2 #follows pemdas
# print(abs(-1)) #math.abs
# print(math.ceil(1.2))


# #conditional
# is_hot = False
# is_cold=True
# if is_hot:
#     print("it's hot")
# elif is_cold:
#     print("it's cold")
# else:
#     print("guess it's average")
# print('hi')


# conditional operators
# has_high_income=True
# has_good_credit=True
# has_record=False
# if has_good_credit and has_high_income:
#     print("hi")
# if has_good_credit or has_high_income:
#     print("bye")
# if has_good_credit and not has_record:
#     print("good")


# comparison operators
# if "1"==1:
#     print("hi") #no type conversion
# if 1>=1:
#     print('hi')


# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)gs: ')
# if unit.upper()=="L":
#     converted= weight*0.45
#     print(f"You are {converted} kilos")
# elif unit.upper()=="K":
#     converted= weight//0.45 #makes it integer
#     print(f"You are {converted} kilos")
# else:
#     print("put in a legit letter")


# PYRAMID
# i=1
# while i<=5:
#     print("*"*i)
#     i+=1
# print("Done")

# guessing game
# secretNumber = 9
# guess_count = 0
# while guess_count<3:
#     guess=int(input("guess: "))
#     guess_count+=1#numbers are immutable in python
#     if guess ==secretNumber:
#         print("winner winner chicken dinner")
#         break
# else:#this can be executed if you reach the end of the while loop and don't break out of it
#     print("you suck")


#user input game
# running = True
# car_on=False
# while running:
#     inp = input().lower()
#     if inp=="help":
#         print('''
# start - to start car
# stop - to stop car
# quit - to exit program
#         ''')
#     elif inp == "start":
#         car_on = True
#     elif inp=="stop":
#         car_on=False
#     elif inp=="quit":
#         running = not running
#     else:
#         print("Cannot compute")


# loop over elements of strings
# items = "items"
# for item in items:
#     print(item)
# for el in [1,2,3]:
#     print(el)
# for item in range(5,10,2): #start at 5, step 2, end 10
# if you write range(2) it starts at zero and ends at 1, like length
#     print(item)
# for x in range(4):
#     for y in range(3):
#         print(f"{x},{y}")


# numbers = [5,2,5,2,2]
# for el in numbers:
#     string = ""
#     for item in range(el):
#         string+= "x"
#     print(string)
# makes a big F


# accessing "lists" ie arrays works the same as in js


#list operations
# numbers = [1,2]
# numbers.append(20) #push
# numbers.insert(0,10) #insert 10 at position 0
# numbers.remove(1) #removes 1 from list
# numbers.clear() #...
# numbers.append(2)
# number= numbers.pop()
# numbers.append(1)
# numbers.index(50)#gives value error
# print(50 in numbers) #False
# numbers.count(1) #returns number of times 1 is in list
# numbers.sort()#sorts in ascending order
# numbers2 =numbers.copy() #makes a copy at another place in memory


# remove duplicates
# numbers = [1,2,2,3,3,4,5,6]
# for item in numbers:
#     while numbers.count(item)>1 :
#         numbers.remove(item)
# print(numbers)
# numbers =[2,2,3,3,4,5,6]
# uniques=[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)


#tuple, it's immutable
# numbers = (1,2,3)
# #only two methods, count and index


#unpacking which is destructuring
# coordinates = (1,2,3)
# x,y,z = coordinates
# numbers=[1,2,3]
# numbers[1],numbers[0] = numbers[0],numbers[1]


#dictionaries key,value
# customer = { #cant reuse keys
#     "name":"john",
#     "age" : 30,
#     "verified": True
# }
# print(customer["name"])#if no name key it returns an error
# print(customer.get('birthdate'))# if no key of that name, it returns a None object
# print(customer.get('birthdate',"this is a default value"))

# phone =input("gimme phone number: ")
# digits_mapping={
# "1":"one",
# "2":"two",
# "3":"three",
# "4":"four",
# '5':'five',
# '6':'six',
# '7':'seven',
# '8':'eight',
# '9':'nine',
# '0':'zero'
# }
# for ch in phone:
#     print(digits_mapping.get(ch))


# message = "hi there"
# message=message.split(' ') #splits at spaces


# functions
# def greet_user(): #functions in python don't float up
#     print('hi user')
# greet_user()
# def hi(this_is_a_keyword_argument="hello"):
#     print(this_is_a_keyword_argument)
# hi()

# can use keyword arguments creatively
# def my_function(arg1,arg2):
#     print(arg1,arg2)
# my_function(arg2="bye",arg1="hi")
# other people reading this code know what's going on
# always use positional arguments first if you're going to use keyword arguments

# def add(x,y):
#     return x+y
# print(add(1,2))


# error handling with try/except
# try:
#     age = int(input('Age: '))
#     print(100//age)
# except ValueError:
#     print('Invalid input')
# except ZeroDivisionError:
#     print('Invalid value')


# classes
# class CamelCase:
#     def move(self):
#         print("move")
#     def draw(self):
#         print('draw')
# instance1 = CamelCase() #this is an object
# instance1.draw()
# instance1.x=10 #addding methods

# class Point:
#     def __init__(self,x,y):#constructor
#         self.x=x #keyword that refers to this object
#         self.y=y
#     def print_point(self):
#         print(self.x,self.y)
# point1 = Point(1,2)
# point1.print_point()

# extending
# class Mammal:
#     def walk(self):
#         print('walk')
# class Dog(Mammal):
#     pass #tells the interpreter that there's nothing here


# modules
# import converters
# print(converters.lbs_to_kg(150))
# from converters import kg_to_lbs
# from converters import *

# import ecommerce.shipping
# from ecommerce.shipping import calc_shipping
# from ecommerce import shipping


# random module
# import random
# # for i in range(3):
# #     print(random.random())#0-1
# #     print(random.randint(10,20))#10-20
# members=['anthony','joe','steve','mary']
# print(random.choice(members))

# FYI
# import random as ran
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first,second #this will be returned as a tupple


 # path/directories
# from pathlib import Path
# # abosult path
# # c:\\asdsadsadasdasd
# # relative path
# # path=Path("ecommerce")
# # print(path.exists())
# # path2 = Path("emails")
# # path2.mkdir()
# path=Path()
# for file in path.glob('*.py'): #iterator object
#     print(file) #all files in current directory


# PyPI packages other people made
# to use pip you do python -m pip install <package name>
# import openpyxl
# useful for working with excel files
# print(openpyxl)
# this one is stored globally
# to install just for one project, need to make virtual python environment


# machine learning
 # 1. import the data
 # 2. clean the data, make it better
 # 3. split data for training and testing
 # 4. create the model
 # 5. train
 # 6. make prediction
 # 7. evaluate and improve

# here's some code for training a model to predict what somebody will like
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split #splitting dataset into testing and training
# from sklearn.metrics import accuracy_score
#
# music_data = pd.read_csv("C:/Users/antho/.ipynb_checkpoints/music.csv")
# X = music_data.drop(columns=["genre"]) #capital because of convention
# y  = music_data["genre"]
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)#20% used for testing
#
# model = DecisionTreeClassifier()
# model.fit(X_train,y_train)#input and output set
# predictions = model.predict(X_test)#male 21, female 22
#
# score= accuracy_score(y_test,predictions)
# score

# code for saving a model
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.externals import joblib #saving and loading models
#
#
# music_data = pd.read_csv("C:/Users/antho/.ipynb_checkpoints/music.csv")
# X = music_data.drop(columns=["genre"]) #capital because of convention
# y  = music_data["genre"]
#
# model = DecisionTreeClassifier()
# model.fit(X,y)#input and output set
#
# joblib.dump(model,'music-recommender.joblib')

# code for loading a model
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.externals import joblib #saving and loading models
#
# model = joblib.load("music-recommender.joblib")
# predictions = model.predict([[21,1]])
# predictions
