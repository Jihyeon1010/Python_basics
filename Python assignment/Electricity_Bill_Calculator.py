# Input customer information
customer_id = input("Enter customer ID: ")
customer_name = input("Enter customer name: ")
units_consumed = float(input("Enter units consumed: "))

# Define the minimum bill amount
minimum_bill = 100.0

# Calculate the total amount to pay
if units_consumed <= 100:
    total_amount = minimum_bill
elif units_consumed <= 200:
    total_amount = minimum_bill + (units_consumed - 100) * 1.5
elif units_consumed <= 300:
    total_amount = minimum_bill + 100 * 1.5 + (units_consumed - 200) * 2.0
else:
    total_amount = minimum_bill + 100 * 1.5 + 100 * 2.0 + (units_consumed - 300) * 2.5

# Apply a 15% surcharge if the total amount exceeds £400
if total_amount > 400:
    surcharge = total_amount * 0.15
    total_amount += surcharge

# Display the electricity bill
print("\nElectricity Bill")
print("Customer ID:", customer_id)
print("Customer Name:", customer_name)
print("Units Consumed:", units_consumed, "units")
print("Total Amount to Pay: £", round(total_amount, 2))
