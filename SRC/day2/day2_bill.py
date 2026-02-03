total_bill=float(input("Enter the total bill amount: "))
num_people=int(input("Enter the number of people to split the bill: "))
bill_per_person=total_bill/num_people
print(f"Total Bill:{total_bill}.Each person should pay:{bill_per_person}")
print("\nData Types:")
print(f"total_bill is of type: {type(total_bill)}")
print(f"num_people is of type: {type(num_people)}")
print(f"bill_per_person is of type: {type(bill_per_person)}")