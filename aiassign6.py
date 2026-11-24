# Pandas Series and DataFrame

import pandas as pd

n = int(input("Enter number of students: "))

rollno = []
names = []
departments = []
marks_list = []

for i in range(n):
    print("\nEnter details of Student", i + 1)

    r = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))

    rollno.append(r)
    names.append(name)
    departments.append(dept)
    marks_list.append(mark)

# Pandas Series
marks = pd.Series(marks_list)

print("\n--- Pandas Series ---")
print(marks)

# DataFrame
data = {
    "RollNo": rollno,
    "Name": names,
    "Department": departments,
    "Mark": marks_list
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))

print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])