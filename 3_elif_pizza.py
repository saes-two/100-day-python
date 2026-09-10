print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

small_pepperoni = 2
medium_large_pepperoni = 3
cheese = 1

bill = 0

if size == "S":
    bill += small_pizza
    if pepperoni == "Y":
        bill += small_pepperoni
elif size == "M":
    bill += medium_pizza 
    if pepperoni == "Y":
        bill += medium_large_pepperoni
elif size == "L":
    bill += large_pizza
    if pepperoni == "Y":
        bill += medium_large_pepperoni
else:
    print("You typed the wrong input.")

if extra_cheese == "Y":
    bill += cheese

print(f"Your final bill is: ${bill}")