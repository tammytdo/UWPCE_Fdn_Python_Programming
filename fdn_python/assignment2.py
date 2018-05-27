"""

Assignment 02

In this activity you will use what you've learned about math and string operations to create a Car Salesman program. 

"""

# Gather the following user input and store each item as a variable: 
# Purchaser name
purchaser_name = input("Enter purchaser name: ")
# Purchaser address
purchaser_address = input("Enter purchaser address: ")
# Purchaser phone number (entered as 503-555-1211)
purchaser_phone = input("Enter purchaser phone in the format XXX-XXX-XXXX: ")
# Car Make/Model
car_make_model = input("Enter car make and model: ")
# Purchase Price
purchase_price = float(input("Enter purchase price: "))

# After the user inputs the above information, your program should add the following values to the sale price:
# Sales tax as a percent of sale price
sales_tax = float(purchase_price * .1)
# Licensing fee
license_fee = float(50)
# Dealer prep fee
dealer_fee = float(100)
# Calculate total cost (as a float)
total_cost = float((purchase_price + sales_tax + license_fee + dealer_fee))

# Assign the car a unique ID composed of the last four letters of the purchaser's last name and their area code, separated by an underscore
unique_id_first_part = purchaser_name[-4:]
unique_id_last_part = (purchaser_phone.split("-", 2)[0])
print(unique_id_last_part)

unique_id = unique_id_first_part + "_" + unique_id_last_part
print(unique_id)

# Print out the information to the screen, with the same line breaks as shown in the example below
print("Purchaser name: " + purchaser_name)
print("Address: " + purchaser_address)
print("Phone: " + purchaser_phone)
print("Car make and model: " + car_make_model)
print("Purchase price: $",  purchase_price)
print("Sales tax: $", sales_tax)
print("License fee: $", license_fee)
print("Dealer fee: $", dealer_fee)
print("total_cost: $", total_cost)
print("Unique ID: " + unique_id)


