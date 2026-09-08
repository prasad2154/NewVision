"""
Exception Handling in Python----------------------------------------------------------->>>>>>>>>>>>-----------------------------------------------------------------------
# Exception handling for error handling in python
# we can use try and except block to handle the error in python

# example of exception handling
try:
    print(10/0)  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("Hello")
for i in range(4):
   print(i)

g=[1,2,3,4]
try:
    print(g[5])  # This will raise an IndexError
except IndexError:
    print("Error: Index out of range.")
# print(g[-1])  # This will raise an IndexError

# HOW??
try:
    #code that may raise an exception
except ExceptionType:
    #code to handle the exception
else:
    #code to execute if no exception occurs
finally:
    #code that will always execute, regardless of whether 
    # an exception occurred or not

try:
    # print(a) #test with exception
    print("Hello")#without exception
except NameError as e:
    print("Error:", e)
else:
    print("No error occurred.")
finally:
    print("The block always executes.")

# Named exception handling
try:
    print(19/0)  # ZeroDivisionError
    #print(10/'a') # TypeError
    #print(t) # NameError
    # ValueError, IndexError, KeyError, AttributeError, FileNotFoundError, IOError, ImportError, ModuleNotFoundError
except ZeroDivisionError as e:
    print('Error:',e)
except TypeError as e:
    print('Error:',e)
except NameError as e:
    print('Error:',e)

If you want to handle multiple exceptions in a single except block, you can use a tuple () to specify the exception types. Here's an example:

try:
    # print(19/0)  # ZeroDivisionError
    #print(10/'a') # TypeError
    print(t) # NameError
    s=[]
    print(s[5]) # IndexError
    # ValueError, IndexError, KeyError, AttributeError, FileNotFoundError, IOError, ImportError, ModuleNotFoundError
except (ZeroDivisionError, TypeError, NameError, IndexError) as e:
    print('Error:', e)

    # exception handling using base class Exception
try:
    # print(19/0)  # ZeroDivisionError
    #print(10/'a') # TypeError
    # print(t) # NameError
    s=[]
    print(s[5]) # IndexError
    # ValueError, IndexError, KeyError, AttributeError, FileNotFoundError, IOError, ImportError, ModuleNotFoundError
except (Exception) as e:
    print('Error:', e)
   
# Creating an exception using raise keyword
num = int(input("Enter a number: "))
if num < 0:
    raise ValueError("Negative numbers are not allowed.")
else:
    print("You entered:", num)
 -----------------------------------------------------------------------------------------------------------------------------------
 

# ATM CASH WITHDRAWAL EXCEPTION HANDLING

try:
    balance=10000
    amount=int(input("Enter the amount to withdraw: "))
    if amount>balance:
        raise ValueError("Insufficient balance.")
except ValueError as e:
    print("Transaction failed:", e)
else:
    balance -= amount
    print("Transaction successfull.Remaining balance:", balance)
finally:
    print("Transaction successfull")
# file handling operations
try:
    with open('students.txt', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("Error: The file 'students.txt' was not found.")
    with open('students.txt', 'w') as f:
        f.write("Name, Age, Marks\n")
        f.write("Prasad, 22, 85\n")
        f.write("Rahul, 23, 78\n")
        f.write("Amit, 21, 90\n")
else:
    print("File read successfully.")
    print("Data from the file:")int("Thank you for using our ATM service.")

finally:
    print("File handling operation completed.")


# solve 5 use-cases 

# 1. Division calculator
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Calculation completed.")


# 2.Login system
correct_username = "prasad_2154"
correct_password = "1234"

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username or password != correct_password:
        raise ValueError("Invalid username or password")

except ValueError as e:
    print("Login failed:", e)

else:
    print("Login successful!")
    print("Welcome", username)

finally:
    print("Login process completed.")

# 3. Shopping cart

price = 500

try:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    total = price * quantity

except ValueError as e:
    print("Order failed:", e)

else:
    print("Order successful!")
    print("Total amount:", total)

finally:
    print("Shopping process completed.")

# 4.student marks with percentage validation
try:
    marks = []
    for i in range(3):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
        marks.append(mark)
except ValueError as e:
    print("Invalid marks:", e)
else:
    total = sum(marks)
    percentage = total / len(marks)
    print("Total marks:", total)
    print("Percentage:", percentage)
finally:
    print("Student marks validation completed.")


# 5.Hotel Room Booking
try:
    rooms_available = 5
    rooms_requested = int(input("Enter number of rooms to book: "))

    if rooms_requested <= 0:
        raise ValueError("Number of rooms must be greater than zero")
    elif rooms_requested > rooms_available:
        raise ValueError("Not enough rooms available")
except ValueError as e:
    print("Booking failed:", e)
else:
    print("Booking successful!")
    print("Rooms booked:", rooms_requested)
finally:
    print("Hotel room booking process completed.")

    

* Decorator
* Generator
* Multithreading
* Logging
* GIL
"""