# -*- coding: utf-8 -*-
"""mah _learning_worksheet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nef4BzPyAbawvdyiVSxuUxy8T7VM07O3
"""

print("Hello world")

print("This is class")
print("I am AI Trainer")

print("This is class", end="\n") 
print("I am AI Trainer")



"""## String"""

print("Hello world")                                 # 1st type

print('Hello world')                                  # 2nd type

print("""Hello world""")                               #3rd type

print('''Hello world''')                               #4th type

print(''Hello world'')

print("hello
world")                                                          # interpreater print the single line output

print("hello"
"world")

print("""Hello 
world""")                                                       # 3 rd type multiple-line output

print("""He
                      llo 
        world """)                                                # IN 3rd and 4th type Its calculate the space also

print("Hello world ")
print("I am AI Trainer")

print("Hello world" , end="\n")
print("I am AI Trainer")

print("Hello world "); print("I am AI Trainer")

print("mango" , "Apple", "Kiwi")

print("mango" , "Apple", "Kiwi", sep=" ")

print("Hello world" , end="lover")
print("I am AI Trainer")

print(r"Hello \nworld" , end="\n")
print("I am AI Trainer")                  #raw string r

print("Hello world" , end="\t")
print("I am AI Trainer")



"""# Variable

1> A variable never start with number [0-9]

2> A variable never contain special character [*/@#$%^&*...etc]

3> A variable can contain underscore "_"

4> A variable should be eassy to read
"""

1class=10

abc&=10

a_=10

_=10                                            # underscore itself a variable

print(_)



"""# Comment

Python have single line comment

comments start with '#'

python interpreater never read the comments

comment use to explain our code
"""

"""This is class
and I am Trainer"""                 #?

b=# "she is ready to go "
print(b)

a="""This is class
and I am Trainer"""
print(a)

"""## Use Cases"""

print("Tanushree "shree"")

print("Tanushree \"shree\"")                                      #backslash hide the property of special character

print("Tanushree 'shree'")

print("Tanushree \n shree ")

print("Tanushree \\n shree ")

print('tanu "shree"')

print("""kathak "dance" is a tradiational form """)

print("""kathak "dance"""")

print("""kathak "dance" """)

print('''kathak 'dance' is a tradiational form ''')

"""# Interpreter Types

1. Cpython
2. Jython
3. Rodpython
4. Ipython
5. Pipi

## Input
"""

print("kindly enter your age:")                     # we can use string as a input statement

input("kindly enter your age:")

a=input("kindly enter your age:")                                 # input accept all values in the form of string

print(a)

print(type(a))

a=int(input("kindly enter your age:"))

print(type(a))

a=int(input("kindly enter your age:"))                          #use case



"""# Data Types

1. Int
2. Float
3. Str
4. List
5. Tuple
6. Set
7. Dict
8. Bool

# Int

Integer datatypes base is 10 [0-9]

Integer datatypes is not iterable

Integer constructor is "int()"

# Casting 

Types casting is method to convert the variable datatypes into a different datatypes to match the operation required
"""

a=10
print(type(a))

b=20.0
print(type(b))

c=int(b)
print(c)
print(type(b))                                # using int() contructor we do coversion of float to integer

"""## Float"""

a=10.0
print(a)
print(type(a))

b=10.
print(b)

c=2e10
print(c)
print(type(c))              # by default e = 10.0

d=2*10**10
print(d)

"""## Str

string is a set of sequence

contructor of str is 'str'

string support indexing

string support slicing 

string is immutable( we can't change it)
"""

#String is a set of sequence 
a="Krishna"
print(a)

print(a[0])

print(a[-1])

"""# slicing """

a="krishna"
print(a[1:6])

print(a[1:6:1])

print(a[1:1000:1])

print(a[1::1])

print(a[0::])

print(a[::])

# when start index doesnt lies in a range
print(a[10::])                                # no output

#how to print reverse order
print(a[6::-1])

print(a[::-1])

a="fga266shdhjsskkskahyetwvxaheuwejsndndskxcnxkxloizooooooooooooooovceedcccjxkixdm4458224sdbf9f63bvbdhjd3250xxbhshsw"
len(a)

# len function also count the space 
b="                                                                                                   "
len(b)

(2/3)+(2/3)

# negative index
a="Tanushree"
print(a[-1:-10:-1])

b="tanushree sahu"
print(b[-1:1000000:-1])

b="tanushree sahu"
print(b[-1:1000000:])

b="tanushree sahu"
print(b[-1::])

"""## Concatination"""

a="Tanushree"
b="Sahu"
print(a+" "+b)

print(a*5.0)

print(a*3)

"""# List 

list is a set of sequence of elements

list is mutable (changeable )

list constructor is list()

list literal is "[ ]" ( to create empty list faster)

list support indexing and slicing both
"""

a=[]                    #empty list
a

b=list()
b

c= list()
c

c=[1,"Tanushree",1.0]
c

print(c[1][6])

d=[1,2,3,4,[3,1,["K","R","I"],4,6],3,4,5]                           # slicing

d[4][2][1]

print(d[2:6:1])

print(type(d))

d.append(1)

d

d.append(1,2)

d.append([11,2])

d

#copy method 

n=[1,2,3,4]
m=n                #shallow copy

m

m.append(1999)

m

n

#deep copy

m=n.copy()

m

m.append(109011)

m

n

"""# Tuple

tuple is immutable (not changable )

tuple is a set of sequence of elements

tuple constructor is tuple()

tuple literal is ()

tuple is faster than list 

tuple support indexing and silicing
"""

tup1=()                #tuple iteral ()

print(tup1)

print(type(tup1))

tup2=tuple()                #tuple constructor is tuple()

print(tup2)
print(type(tup2))

tup3=(1,2,3,4)

print(tup3)

print(tup3[0])              #indexing

print(tup3[-1])

tup4=(1,2,3,(5,3,2,2),2,4,5,6)

print(tup4[3][2])

tup5=[i for i in range (20,50,2)]

tup6=tuple(tup5)                       #tuple contructor to creat a list into tuple

print(tup6)

# tuple support slicing

print(tup6[2:9:1])

print(tup6[0:10000])

print(tup6[::])

#tuple has two methods
#  1. count
# 2 . index

tup6.count(22)

tup6.index(24)

tup7=list(tup6)

tup7

tup7.append(49)

tup7

tup6=tuple(tup7)

tup6

"""# Set

set is unordered set ofsequence of elements

set constructor set()

set is mutable

set use hashing table

set doesnot allow duplicate values 

set does not contain mutable datatypes likes set ,dict , list 
"""

set1=set()

set1

set2={1}

print(set2)

print(type(set2))

set2.add(2)

set2

# use case
set2.add(1,2)

set2.add({1,2})

set2.add([1,2])

set2.add((1,2))

set2

set3={1,3,4}

set2.difference(set3)

set2.difference_update(set3)

set2

set4={1,2,3,4,4,4,5,6,5,6,4}

set4                             #it does not contain duplicate value

#methods of set

a={1,2,3,4,5}
b={3,4,5,6,7,8}

a.difference(b)

a

a.difference_update(b)

a

b

print(a.discard(5))

a

a.clear()

a

a.update({1,2,3,4})

a

a.add({4,5,6,7,8})

a.update([6,8,9,10])

a

a.add((11,12))

a

a.update(100002)

a.update(10.0)

a.update("Tanushree")

a

A={1,2,3,4}

B={1,2,3,4,5,6}

A.issubset(B)

A.issuperset(B)

B.issuperset(A)

A.pop()

A

C={1,2,3,4}
D={1,3,7}

C.union(D)

C.remove(4)

C

C.remove(7)

C.discard(4)

C

D

C.symmetric_difference(D)

C.symmetric_difference_update(D)

C

"""# Dictionary

dictionary constructor is dict( )

dictionary literal { }

dictionary contain keys : values combination

Its mutable

key treat as index 

key always unique
"""

a=dict()

print(a)
print(type(a))

b={}
print(b)
print(type(b))

c={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f"}

c.keys()

c.values()

c.items()

c.get(6)

c.get('f',"key is not found")

c.pop()

c.pop(1)

c

c.popitem()                    #this method works on to remove the last key values pair of dictionary

c

c.setdefault(1)

c

c.setdefault(5,"tanushree")

c

c.setdefault(6,'tanvi')

c

c[6]="shree"

c

c[6]=("anuj","anupama")

c

c[1]={'studentname':"pakhi","fathersname":"vanraj","mothersname":"anupama"}

c

c[1]["fathersname"]

d={{1,2,3}:"shree"}

d={(1,2,3):"shree"}

d



"""# Complex

1. Real Number 
2. Imaginary number 
eg.: (1+1j)


"""

print(0*j)

print(0j)

a=0j
print(a)
print(type(a))

complex(2)                     # complex constructor

complex(2,2)

complex(0,0)

"""# Boolean

boolean constructor is bool()

boolean return either True or False
"""

bool(1)

bool(0)

bool(-1)

bool(True)

bool("True")                           # when True keyword is converted into another data type is given true

bool(False)

bool("False")

bool({})              #dict

bool({1})        #set

bool({False})

bool(0)

bool({0})

bool({{}})            # outer : set , inner: dict ; set only contain immutable data type

bool({[]})

bool({()})

bool({({})})

print(type(({1:"tanu"},)))

a=(1)
print(type(a))

a=(1,)
print(type(a))

print(type({({1:"tanu"},)}))

bool(0.0)

bool()

bool([])

bool({{}})

bool([[]])

bool({1:"tanushree"})

bool({})

"""# operators


Arithmetic operator : *,**,/,//,-,+,%

Bitwise operator : & , | , << (left shift), >> right shift , ~ tild

membership operator : in , not in 
"""

a=10
b=20

a,b=10,20

print("a value : ",a)
print("b vaue : ", b)

#swap without using 3rd variable

# 1 way 
a,b=20,10

print("a value : ",a)
print("b vaue : ", b)

# 2 way 

x=20
y=10

x=x+y
y=x-y
x=x-y

print("x value : ",x)
print("y vaue : ", y)

# using 3rd variable for swap 

x=5
y=10

temp=x
x=y
y=temp

print("x value : ",x)
print("y vaue : ", y)

"""operator"""

a=10
b=20
a+b

a-b

a/b

a*b

a**b

c=10.0
d=20

c**d

print(2e10)

e=10.0
f=3

e/f

e//f

e%f

10.0%3.0

# Membership operator

"python" in "python is funny language"

a="python"
b="python is funny language"

a in b

print(id(a))

b[0:6]

print(id(b[0:6]))

a="python"
b="Python is funny language"

a in b

a not in b

a=10
b=20
a is b

a is not b

#shorthand

a=10

a+=1                        # a=a+1
a

a=10

b=20

a-=b

a

a=10
b=20
a/b

a/=b

"""Bitwise operator 

Number system is cs 

Binary number system (0,1)

octal number system (0,1,2,3,4,5,6,7)

Decimal number system (0,1,2,3,4,5,6,7,8,9)

Hexadecimal number system (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
"""

~12

~14

~(-12)

a=10
b=11

a|b

"""23-08-2022

## IF else *elif*
"""

user=input("Hello world how are you:")

user

user=input("hello world how are you :")
if user=="fine":
  print("I am fine too")
else:
  print("am i audiable?")

user=input("hello world how are you :")
if user=="fine":
  print("I am fine too")
else:
  print("am i audiable?")

user=input("hello world how are you :")
if user=="fine" or user=="good":
  print("I am fine too")
else:
  print("am i audiable?")

user=input("our first talk:")
user1=input("second talk:")

if user=="sorry" and user1=="how are you?":
  print("Its fine, now")
else:
  print("i don't wanna to talk")

num1=int(input("enter Ist no:"))
num2=int(input("enter 2nd no :"))


if num1==10 and num2==20:
  print("sum: ",num1+num2)
else:
  print("I am not able to add")

num1=int(input("enter Ist no:"))
num2=int(input("enter 2nd no :"))


if num1==10 and num2==20:
  print("sum: ",num1+num2)
else:
  print("I am not able to add")

"""Nested if else"""

num1=eval(input("enter Ist no:"))



if num1==10:
  print("this condition is true with 10")
  num2=eval(input("enter 2nd no :"))
  if num2==20:
    print("sum: ",num1+num2)
  else:
    print("are you crazy")
else:
  if num1==1:
    print("i forget how to add")
  else:
    print("I am not able to add")

"""# Indentation 

Its whitespace at the begining of a line ; to define the block scope 
"""

print("""Welcome to ATM of BOI
        1. change Pin
        2. Balance enquiry
        3.withdrawal
        4.exit""")

user=input("enter you option:")

if user=="1":
  print("welcome to change pin section:")
  print("""
  1.Remember old pin
  2. forget pin""")

  user_pin=input("enter your option :")
  if user_pin=="1":
    print("kindly enter your old pin:")
  elif user_pin=="2":
    print("kindly enter ur number:")
  else:
    print("choose valid option: ")

elif user=="2":
  print("welcome to balance enquiry section: ")
elif user=="3":
  print("welcome to  withdrawal section:") 
elif user=="4":
  print("Thankyou for using our service!!!")
else:
  print("Be in your limit")

"""# LOOP
repeatedly execute the code until a given condition is true ;if condtion false is terminated the loop

1. for loop

2. while loop
"""

for i in "tanushree":
  print(i)

for i in [3,4,"tanu",10.5]:
  print(i)

# range is inbuilt function 

for i in range(10):
  print(i)

for i in range (0,11,1):
  print(i)

for i in range("tanu"):
  print(i)

a='desrghhhnaawffshffffffffffffghhhhksfffffffffffhnnnopnnmajvvvvvvvvvawwwwwwq'

len(a)

for i in  range(len(a)):
  print(i+1,".",a[i])

a="tanushree"

for i in range(0,9,1):
  print(a[i])

a="tanushree"

for i in range(0,10,1):
  print(a[i])

# pattern question 
# *
# **
# ***
# ****
# *****

# We can use nested for loop as well single for loop

for i in range(5):
  for j in range(i):
    print(0,end="")
  print()                         # line change

for i in range(5):
  for j in range(i+1):
    print(0,end="")
  print()

"""# OOps (Object oriented programming structure)

"""

class Ghar:
  def __init__(self):
    #attributes ----- > instance variable 
    self.storey=75
    self.height="1.2km"
    self.room=1000

  def accommodation(self):
    print("I have good accomodation in my ghar ")
  def swimming(self):
    print("I get a swimming section in my ghar")
  def restra(self):
    print("You can get good food in my ghar like restaurent")

Delhi=Ghar()

print(type(Delhi))

Delhi.accommodation()

"""# \__init__ this magic method ( constructor ) call automatically """

print(id(Delhi))

Delhi.storey

Delhi.storey=100

Delhi.storey

name="Tanushree"
print("My name is {}".format(name))

print(f"My name is {name}")

class Intro:
  def __init__(self):
    self.name=""
    self.age=0
    self.location=""

  def Name(self):
    print(f"My name is {self.name}")
  def Age(self):
    print("My age is {}".format(self.age))
  def Location(self):
    print("My location is {}".format(self.location))

tanu=Intro()

tanu.name="tanushree"

tanu.Name()

tanu.age=24
tanu.Age()

tanu.location="Ip extention"
tanu.Location()

"""Class is Blueprint

object is real life object ; 

instance variable or attributes declare with in constructor (def \__init__(self))

self is object

Encapsulation 
 
 hiding the data
"""

class ATM:
  def __init__(self):
    self.pin=""
    self.balance=0
  
  def change_pin(self):
    print("Welcome to change pin section:")
  
  def balance_update(self):
    print("Welcome to balance update section:")
  
  def balance_enq(self):
    print("Welcomt to balance enquiry section:")
  
  def withdrawal(self):
    print("Welcome to withdrawal section:")

tanu=ATM()

tanu.pin

tanu.balance

tanu.pin=1526

tanu.pin

"""1: problem:(create a method inside class to update pin and blance)

we should create a method to change pin inside a class

2: problem:(encapsulation)

we must hide our class variable/instance variable
"""

class ATM:

  def __init__(self):
    self.__pin='0000'
    self.__balance=0
    self.menu()

  def menu(self):
    user_input=input("""Welcome to SBI
    
    Kindly choose one option:
    
    1. Change Pin
    2. Balance Update
    3. Balance Enquiry
    4. Withdrawal
    5. Exit
    """)
    if user_input=='1':
      self.change_pin()
    elif user_input=='2':
      self.balance_update()
    elif user_input=='3':
      self.balance_enq()
    elif user_input=='4':
      self.withdrawal()
    elif user_input=='5':
      print("Thank you to banking with us")
    else:
      print("Be in your limit")
      
  def change_pin(self):
    print("Welcome to change pin section:")
  
  def balance_update(self):
    print("Welcome to balance update section:")
  
  def balance_enq(self):
    print("Welcomt to balance enquiry section:")
  
  def withdrawal(self):
    print("Welcome to withdrawal section:")

tanu=ATM()

tanu.menu()

"""Inheritance"""

class Student:
  def signup(self):
    print("Welcome to signup section")
  
  def login(self):
    print("Welcome to login section")
  def certification(self):
    print("Get you certification now")

class Trainer:
  def signup(self):
    print("Welcome to signup section")
  
  def login(self):
    print("Welcome to login section")
  def commision(self):
    print("Hey man this is your earning")

#14-10-2022
#Class

class Person:
  def __init__(self, first_name, last_name, age):
    self.first_name=first_name
    self.last_name=last_name
    self.age=age

P1=Person("tanu","shree",24)

print(P1.first_name)

class Person:
  def __init__(self, first_name, last_name, age):
    self.person_first_name=first_name
    self.person_last_name=last_name
    self.person_age=age

P2=Person("mony","vyash",25)

print(P2.person_last_name)

#exercise
# creat a laptop class with attributes like brand name ,model_name and price

class Laptop:
  def __init__(self, brand_name, model_name, price):     #attributes
    self.brandname=brand_name                           # instance variable
    self.modelname=model_name
    self.price=price
    self.laptopname= brand_name + ' ' + model_name      



L1=Laptop("Dell","dell2021",45000)
L2=Laptop("HP","hp60023",37000)

print(L1.brandname)

print(L2.laptopname)

# Instance method

class Person:
  def __init__(self,first_name, last_name, age):
    self.first_name =first_name
    self.last_name=last_name
    self.age=age
  
  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  def above_18(self):
    return self.age>18


P1=Person('Tanu','shree',24)
P2 =Person("mohit","sharma",15)
# print(P1.full_name())
print(P2.above_18())


print(Person.full_name(P1))

l=[1,2,3]

# l.clear()   #1-way

list.clear(l)
print(l)

class Laptop:
  def __init__(self, brand_name, model_name, price):     #attributes
    self.brandname=brand_name                           # instance variable
    self.modelname=model_name
    self.price=price
    self.laptopname= brand_name + ' ' + model_name 

  def apply_discount(self,num):
    off_price=(num/100)*self.price
    return self.price - off_price

L1=Laptop("Dell","dell2021",45000)
L2=Laptop("HP","hp60023",37000)

print(L1.apply_discount(10))

"""Inheritance"""

class login_signup:
  def signup(self):
    print("welcome to sign up section ")
  def login(self):
    print("Access through login")

class student:
  def certification(self):
    print("This is your certification")

class trainer:
  def commission(self):
    print("Hey is your income ")

class Phone:
  def __init__(self, brand , model_name ,price):
    self.brand=brand
    self.model_name= model_name
    self._price= max(price, 0)

  def full_name(self):
    return f"{self.brand} {self.model_name}"

  def make_a_call(self,number):
    return f"calling....{number}"




class Smartphone(Phone):
  def __init__(self,brand , model_name , price , ram ,internal_memory, rear_camera):
    super().__init__(brand,model_name,price)
    self.ram = ram
    self.internal_memory= internal_memory
    self.rear_camera= rear_camera

phone=Phone("Nokia","1100",1000)

print(phone.full_name())

smart=Smartphone("redmi","note9",15000,"6GB","64 GB","20 mp")

print(smart.full_name())

newphone= Smartphone("samgsung","sum12345",-50000,"4Gb","32GB","10 mp")

print(newphone._price)

class Phone1:
  def __init__(self, brand , model_name ,price):
    self.brand=brand
    self.model_name= model_name
    if price>0:
      return self._price
    else:
      self._price=0

mobile = Phone1("Tecno","techlife2",-800)

print(mobile._price)

from array import *

array1=array("i",[10,20,2,30,40])
for x in array1:
  print(x)

array1.insert(1,50)

for x in array1:
  print(x)

array1.remove(40)

"""Polymorphism  : one thing many forms 

overloading - having same name & different signatures

overriding 
"""

class Sum:
  def add(self, a, b):
    print(a+b)
  def add(self, a,b,c):
    print(a+b+c)

a=Sum()

a.add(2,3,3)

a.add(2,3)

class Sum1:
  def add(self , a, b, c=0):
    print(a+b+c)

ef=Sum1()

ef.add(2,3)

ef.add(2,5,1)

class play:
  def sayhello(self, name=None):
    if name is not None :
      print(f"Hey {name}")
    else:
      print('Hello')

oj=play()

print(oj.sayhello())

print(oj.sayhello('rashmi'))

#Decorator 

def sub(a,b):
  print(a-b)

def super(fun):
  def inner():
    a=int(input("enter ist no :"))
    b=int(input("enter 2nd no : "))
    if a<b:
      a,b=b,a
      fun(a,b)
    else:
      fun(a,b)
  return inner

val=super(sub)
val()

def dec_function(fun):
  def wrapper_function():
    print("This is great things")
    fun()
  return wrapper_function

def new_function():
  print("This is my trial")

val=dec_function(new_function)
val()

"""**Abstraction**

we can't create a object ;(can't create instantiated)

we using python ABC class through (abc is python module )

Two terms 

*ABC class inherit by our class (child )

*at least one method must be abstract method
"""

from abc import ABC, abstractmethod

class ATM(ABC):

  @abstractmethod
  def change_pin(self):
    print("Welcome to pin section ")

  def balance(self):
    print("balance section you entered")

obj1=ATM()

# iterable : A datatype which contain __iter__() (magic method) is called iterable

from re import X
# How to make our for loop

class Meraloop:
  def __iter__(self):
    self.a=0
    return self
  def __next__(self):
    x=self.a
    self.a=self.a+1
    return x

obj=Meraloop()
iterate1=iter(obj)

print(next(iterate1))
print(next(iterate1))
print(next(iterate1))
print(next(iterate1))

