"""

Assignment 06 - Pizza Functions

Calculate the cost of pizza for movie night.  

"""
#!/usr/local/bin/python3

import math 

# Create the following static (unchanging) variables:
# Pizza cost = $10.00 
pizza_cost = float(format(10, ",.2f"))
# Total slices = 8 
slices_per_pizza = int(8)
# Tax rate of 9.6%
tax = float(format(1.096, ",.3f"))
# Tip rate of 5 -15%
tip = float(format(1.015, ",.3f"))
# Delivery fee of $3.99 
delivery_fee = float(format(3.99, ",.2f"))
#pizza_after_fees = float(format(pizza_cost * tax * delivery_fee, ",.2f"))


# Get user input for the following: 
# You can store these as a single integer, or use a dictionary to map names to values, up to you

def num_people():
    # Number of people who want pizza
    people = int(input("How many people want pizza?: "))
    return people

def num_slices():
    # Average number of slices per person
    slices_per_person = int(input("How many slices per person?: "))
    return slices_per_person

# Calculate how many pizzas to order based on number of people and average slices
def pizza_quantity(people, slices_per_person):
    quantity_slices = people * slices_per_person
    quantity_pizzas = math.ceil(quantity_slices / slices_per_pizza)
    print("Order {} pizzas to have {} slices per person.".format(quantity_pizzas, slices_per_person))
    return quantity_pizzas

def slices_left_over(quantity_pizzas, people, slices_per_person):
    slices_remaining = (quantity_pizzas * 8) - (people * slices_per_person)
    print("There will be {} slice(s) remaining.".format(slices_remaining))
    return slices_remaining

# Total pizza costs
def pizza_before_tip(quantity_pizzas):
    before_tip_cost = pizza_cost * tax
    all_pizzas_cost = before_tip_cost * quantity_pizzas
    print("Cost per pizza with tax, before tip is ${:.2f}.".format(before_tip_cost))
    print("The cost for all pizzas with tax, before tip is ${:.2f}.".format(all_pizzas_cost))
    return all_pizzas_cost

def indiv_cost(all_pizzas_cost, people):
    cost_per_person = all_pizzas_cost / people
    #print("The total cost per person before tip is ${:.2f}.\n".format(cost_per_person))
    return cost_per_person

# Add an option to calculate the tip by person or by slice.
def pizza_after_tip(all_pizzas_cost, cost_per_person):
    tip_percent = float(input("What percent do you want to tip?: "))
    percent = (tip_percent / 100) + 1
    after_tip_cost = all_pizzas_cost * percent
    return after_tip_cost

def pizza_after_delivery(after_tip_cost, people):
    delivery = input("Will this pizza be delivered? Yes or no: ")
    delivery = delivery.lower()
    if delivery == "yes":
        pizza_with_delivery = after_tip_cost + delivery_fee
        print("Cost per person after tip and delivery is now ${:.2f}".format(pizza_with_delivery / people))
        print("Cost for all pizzas after tip and delivery is now ${:.2f}.".format(pizza_with_delivery))
    elif delivery == "no":
        print("Cost per person after tip, without delivery, is now ${:.2f}".format(after_tip_cost / people))
        print("Cost for all pizzas after tip, without delivery, is now ${:.2f}.".format(after_tip_cost))
    else: 
        print("Enjoy!")

if __name__ == "__main__":
    ppl = num_people()
    slices = num_slices()
    piz_quantity = pizza_quantity(ppl, slices)
    left_over = slices_left_over(piz_quantity, ppl, slices)
    before_tip = pizza_before_tip(piz_quantity)
    per_person = indiv_cost(before_tip, piz_quantity)
    after_tip = pizza_after_tip(before_tip, per_person)
    pizza_after_delivery(after_tip, ppl)

# Update your pizza script to read in a file (txt or csv) of how many slices of pizza different people want (ex: Daniel, 3) and calculate the cost for each person individually.
