"""
#docstring---used for multiline comment
----------------------------------------

Class and Object

class--is a template for creating objects,blueprint for creating objects
class=properties(variables)+ behaviors(methods)


class Car:
    #properties of class
    doors = 4
    engine = 1
    e_name="TURBO"

    # behaviour-operations or methods
    def drive(self):
        print("car is driving")

    def drift(self):
        print("car is drifting")

#Object -- It is an instance of a class. 
# It is a real-world entity that has state and behavior. An object is created from a class and can access the properties and methods defined in the class.
# call the class to create an object

bmw = Car()  # bmw is an object of class Car
print(bmw.e_name)
bmw.drive()
bmw.drift()
bmw.doors = 2
print(bmw.doors)

baleno = Car()  # baleno is an object of class Car
print(baleno.e_name)
baleno.drive()
baleno.drift()


class Human:
    eyes = 2
    head = 1
    hands = 2

    def walk(self):
        print('Walking')

# how many objects we can create--> We can create N objects
prasad = Human()
print('Head:',prasad.head)
prasad.walk()

ravan = Human()
ravan.head = 10
print('Head:',ravan.head)


#What is self ?
# it is a reference variable that refers to the current instance of the class. It is used to access the properties and methods of the class in python. It is a convention to use self as the first parameter of the methods in a class.
class Human:
    eyes = 2
    head = 1
    hands = 2

    def sample(self):
        print('Hello good morning')
    def info(self):
        print('Eyes:',self.eyes)
        print('Head:',self.head)
        print('Hands:',self.hands)
        # calls sample inside info
        self.sample()
    # To access the members of the class we need to use self keyword. 
    # It is a reference variable that refers to the current instance of the class. 
    # It is used to access the properties and methods of the class in python. It is a convention to use self as the first parameter of the methods in a class.
h1 = Human()
h1.info()
# h1.sample()
-------------------------------------------------------------------------------------------------
from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(x_train, y_train)
model.predict(x_test)
model.score(x , y)


# what is constrctor?
# constructor is nothing but class calling
# it is used to allocate a memory to create an object
#
In OOP when we call a constructor then it calls __init__ method of the class.
 It is a special method that is called when an object is created. 
 It is used to initialize the properties of the class. It is defined using the def keyword and it takes self as the first parameter. It can also take other parameters to initialize the properties of the class.

class Test:
    def __init__(self):
        print('Constructor is called')
    def sample(self):
        print('Hello good morning')
t1=Test()  # constructor is called

# __init__ is a magic method
# dunder method--- double underscore method in prefix and suffix

# what is difference between function and method?
# function is a block of code that performs a specific task. It can be called from anywhere
# method is a function that is defined inside a class and is called on an object of that class.

class Bank:
    def credit(self,amt,balance=0):
        # to access updated balance in other method make it instance variable
        self.balance = balance
        print('Balance in Credit Rs.',self.balance)
        print('Amout Credited Rs.',amt)
        self.balance += amt
        
    
    def debit(self,amt,balance=0):
        print('Intial amount Rs.',self.balance)
        self.balance -= amt # perform deduction
        print('Amount after deduction of Rs.',amt,'is Rs.',self.balance)

b1 = Bank()
b1.credit(20000,4000)
b1.debit(2500)
#b1.credit(1000,5000)
-------------------------------------------------------------------------------------------------------------------


Pillars of OOP
1.Inheritance
2.Encapsulation
3.Polymorphism
4.Abstraction(skip)

1. Inheritance
Building the parent child relationship among the classes
we will have one class as a Parent and another class/s as child



class RBI:
    def rules(self):
        print('RBI rules are applicable to all banks')

class SBI(RBI):
    def policy(self):
        print('SBI policy is applicable to SBI bank only')

s1 = SBI()

s1.policy()  # calling child class method
s1.rules()  # calling parent class method


    Types  of Inheritance
    1. Single Inheritance
    2. Multiple Inheritance
    3. Multilevel Inheritance
    4. Hierarchical Inheritance
    5. Hybrid Inheritance
    -------------------------------------------------------------
    Q.what is the difference between single and multiple inheritance?
    Ans: In single inheritance, a child class inherits from a single parent class. In multiple

    q. what is dff multilevel and multiple inheritance?
    Ans: In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another parent class. In multiple inheritance, a child class can inherit from multiple parent classes.


# Example of Multilevel Inheritance
class Grandfather:
    def bike(self):
        print('Grandpas Bike')

class Father(Grandfather):
    def car(self):
        print('Father car')


class Mother(Father):
    def money(self):
        print('Mother money')

class Child(Mother):
    pass

c1 = Child()
c1.money()
c1.car()
c1.bike()
"""
class Grandfather:
    def money(self):
        print('Grandpas Money')

class Father(Grandfather):
    def money(self):
        print('Father Money')
        super().money()

class Mother(Father):
    def money(self):
        print('Mother Money')
        super().money()

class Child(Mother):
    pass

c1 = Child()
c1.money()
