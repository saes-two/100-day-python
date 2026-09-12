from ast import ListComp
from operator import le
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

list_char = []
password = ""
words = 0

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(0, nr_letters):
    letter = random.choice(letters)
    list_char.append(letter)

for i in range(0, nr_symbols):
    simbol = random.choice(symbols)
    list_char.append(simbol)

for i in range(0, nr_symbols):
    num = random.choice(numbers)
    list_char.append(num)

password_char = random.sample(list_char, len(list_char))
final_password = "".join(password_char)

print(list_char)
print(password_char)
print(f"Your password is: {final_password}")