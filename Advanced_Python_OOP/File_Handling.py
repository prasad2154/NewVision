"""
File Handling perform operations over the files

create
write
read
append

to create a file:
w: create a new file and overwrite the contents
a: create a new file and append the contents
x:create a new file only ones and 



f=open('test.txt','w')
  #create a new file and overwrite the contents
f.write('Hello World\n') #write the contents to the file
f.write('12,43,5,32,5315,53277\n')
f.close() #close the file
f=open('test.txt','a') #create a new file and append the contents
f.write('Hello World python \n') #write the contents to the file
f.close() #close the file

for auto closing file
    use with statement
  
with open('a.txt','w') as f:
    f.write("Hello, this is a new file.\n")  # Write to the file
    f.write("with auto close")  # This will not raise an error because the file is open

# The file is automatically closed after the 'with' block
    f.write("This line will not be written because the file is closed.\n")  # This will raise an error
print("File operations completed successfully.",f.closed)  # Check if the file is closed    
  

# In write method u must have to pass only string not any other datatype
with open('a.txt','w') as f:
    f.write(123456)
# Assignmet :
check append mode and exclusive mode

msg=input("enter the message to write in the file:  ")
msg=msg.split()
with open('a.txt','w') as f:
    f.write('\n'.join(msg))

with open('a.txt') as f:
 data = f.read()  # Read the entire file
print(data)  # Print the data read from the file
# use these options at the place of f.read()

# f.readline()
with open('a.txt') as f:
 data = f.readline()  # Read the entire file
print(data)

# f.readlines()
with open('a.txt') as f:
 data = f.readlines()  # Read the entire file   


-------------------------------------------------------------------------------------------------------------------
Exception handling for error handling in python
we can use try and except block to handle the error in python

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


#  Assignment
# 1.Try to read and write over pdf,excel,and csv files

# 1. CSV File — Read and Write

# For CSV files, we can use Python's built-in csv module.

# Read CSV File:
import csv

with open("students.csv", "r") as file:
    data = csv.reader(file)

    for row in data:
        print(row)

# Write csv file

import csv

students = [
    ["Name", "Age", "Marks"],
    ["Prasad", 22, 85],
    ["Rahul", 23, 78],
    ["Amit", 21, 90]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully")

# 2. Excel File — Read and Write

import pandas as pd

data = {
    "Name": ["Prasad", "Rahul", "Amit"],
    "Age": [22, 23, 21],
    "Marks": [85, 78, 90]
}

df = pd.DataFrame(data)

df.to_excel("students.xlsx", index=False)

print("Excel file created successfully")

# Read Excel File

import pandas as pd

df = pd.read_excel("students.xlsx")

print(df)
"""

# 3. PDF File — Read and Write
# For reading PDF, we can use PyPDF2.
# For creating/writing PDF, we can use reportlab
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("students.pdf")

pdf.drawString(100, 750, "Student Details")
pdf.drawString(100, 700, "Name: Prasad")
pdf.drawString(100, 670, "Age: 22")
pdf.drawString(100, 640, "Marks: 85")

pdf.save()

print("PDF created successfully")

# Reading PDF File
from PyPDF2 import PdfReader

reader = PdfReader("students.pdf")

for page in reader.pages:
    text = page.extract_text()
    print(text)