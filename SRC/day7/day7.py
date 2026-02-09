file = open("sample.txt", "w")
file.write("Hello, this is a file handling example.")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#context manager with open()
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


#error handling with try-except
try:
   with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found. Please check the file name and try again.")

print("\n")
#csv file handling
import csv
with open("data.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n")

#xlsx file handling
import openpyxl
workbook = openpyxl.load_workbook("data2.xlsx")
sheet = workbook.active
for row in sheet.iter_rows(values_only=True):
    print(row)