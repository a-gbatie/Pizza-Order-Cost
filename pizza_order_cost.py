# Pizza Order Cost Calculator
# This program calculates the total cost of a pizza order.
# The total includes pizza size, toppings, and delivery fees.

"""
START

1. Ask the customer for their pizza size.

2. Ask how many toppings they want.

3. Ask for their delivery distance in miles.

4. Determine the pizza price:
   IF small, price = $8
   ELSE IF large, price = $12
   ELSE if neither, price = $0

5. Calculate topping cost:
   Number of toppings * $1

6. Calculate delivery cost:
   IF distance = 0, delivery = $0
   ELSE IF distance <= 5, delivery = $2
   ELSE delivery = $2 + $1 per extra mile

7. Add all costs together:
   Total = Pizza + Toppings + Delivery

8. Display the total cost.

END
"""

# Get order information from the customer
pizza_size = input("Enter pizza size (small or large): ")

toppings = int(input("Enter number of toppings: "))

distance = float(input("Enter delivery distance in miles: "))

# Determine the price based on the pizza size
if pizza_size == "small": # Check if pizza size is small
  pizza_price = 8 # If yes, charge $8
elif pizza_size == "large": # Check if pizza size is large
  pizza_price = 12 # If yes, charge $12
else:
  pizza_price = 0 # If neither small or large, charge $0
  print("Invalid pizza size") # Print this statement because only small or large sizes are accepted
  
# Calculate the cost of additional toppings
toppings_cost = toppings * 1

# Calculate the delivery fee
if distance == 0: # If order is a pickup aka no distance
  delivery_fee = 0 # Charge $0
elif distance <= 5: # If delivery distance is 5 miles or less
  delivery_fee = 2 # Charge $2
else:
  delivery_fee = 2 + (distance - 5) * 1 # Otherwise if distance is further than 5 miles, charge $1 for each additional mile
  
# Calculate total cost
total_cost = pizza_price + toppings_cost + delivery_fee

# Display the total cost
print(f"Your total cost for this order is ${total_cost:.2f}.")