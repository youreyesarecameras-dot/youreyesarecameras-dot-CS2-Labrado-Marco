# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ").strip()

# validating name
while name == "":
    print("Name must not be blank.")
    name = input("Enter customer name: ").strip()
    if name != "":
      break

previous = float(input("Enter previous meter reading: "))

# validating that previous reading is at least 0
while previous < 0:
    print("Previous reading must at least be 0.")
    previous = float(input("Enter previous meter reading: "))
    if previous >= 0:
        break

current = float(input("Enter current meter reading: "))

#validating that current reading is at least equal to previous reading
while current < previous:
    print("Current reading must at least be equal to the previous reading.")
    current = float(input("Enter current meter reading: "))
    if current >= previous:
        break

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
