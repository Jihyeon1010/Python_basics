customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
unit_consumed = float(input("Enter the units consumed: "))

if unit_consumed < 100:
    total_amount = 100  
elif unit_consumed <= 400:
    total_amount = unit_consumed * 1.5  
else:
    total_amount = unit_consumed * 1.5  
    surcharge = 0.15 * total_amount  
    total_amount += surcharge

print("Electricity Bill")
print("Customer ID:", customer_id)
print("Customer Name:", customer_name)
print("Units Consumed:", unit_consumed)
print("Total Amount to Pay: £", total_amount)
