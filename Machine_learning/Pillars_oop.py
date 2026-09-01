"""
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


Key Points

Public: Accessible everywhere.

Protected: Accessible in class and subclasses (by convention).

Private: Accessible only within the class (name mangling possible).

Python relies on developer discipline rather than strict enforcement.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2.Encapsulation



class Sample:
    a = 100 # public
    _b = 200  # protected 
    __c = 300  # private

s1 = Sample()
print(s1.a) # accessing public attribute
print(s1._b)  # Accessing protected attribute
#print(s1.__c)  # Accessing private attribute
# Private attributes can be accessed using name mangling
print(s1._Sample__c)  # Accessing private attribute using name mangling

# we cannot access private attributes directly from outside the class, 
# but we can access them using name mangling. This is a way to prevent accidental access to private attributes, but it is still possible to access them if needed.

class Sample:
    def m1(self):
        print('Public')
    def _m2(self):
        print('Protected')
    def __m3(self):
        print('Private')
s1 = Sample()
s1.m1()  # Public method
s1._m2()  # Protected method
#s1.__m3()  # Private method (will raise an AttributeError)

# call using name mangling
s1._Sample__m3()


class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        super().__init__(name, base_pay)
        self.sales_incentive = sales_incentive

    def get_pay(self):  # Overriding parent method
        return self.base_pay + self.sales_incentive


john = SalesEmployee("John", 5000, 1500)

print(john.get_pay())  # Output: 6500

---------------------------------------------------------------------------------------------------------------

class Father:
    def money(self):
        print('Fathers money')

class Mother:
    def money(self):
        Father.money(self)  # Call the method from Father class
        print('Mothers money')

class Child(Mother,Father):
    pass
c1 = Child()
c1.money()  # Calls the method from Mother class due to MRO (Method Resolution Order)

# CHECK MRO
print(Child.__mro__)  # Output: (<class '__main__.Child'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>)


# ASSIGNMENT: CHECK FEW EXAMPLES OF MRO

Example 1: Single Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    pass

b = B()
b.show()

print(B.mro())

       A
      / \
     B   C
      \ /
       D


class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show()

print(D.mro())
------------------------------------------------------------------------------------------------------------------------------------------
4.Polymorphism-
Poly(Many)+Morphism(Forms)
simple norm with multiple forms
we technically implement polymorphism through method overriding and method overloading. 
In Python, we can achieve polymorphism through method overriding.

# operator overloading/operator level polymorphism
# as + operator is overloaded to perform addition of two numbers and concatenation of two strings
print(10+20) #addition of 2 numbers
print('Hello'+" "+'World') # concatenation of two strings
------------------------------------------------------------------------------------------------------------------------------------------
we have 3 differnt types of overloading in python
1. Operator Overloading-->Possible
2. Method Overloading-->not possible
3. Constructor Overloading-->not possible

class Sample:
    def m1(self):
        print('No argument method')
    def m1(self,a):
        print('One argument method')
    def m1(self,a,b):
        print('Two argument method')
    def m1(self,a,b,c):
        print('Three argument method')
s1 = Sample()
s1.m1(10,20,30)  # calling method with 3 arguments
s1.m1(10,20)  # wont run
s1.m1(10)  # wont run
s1.m1()  # wont run
"""  