import math

print("Pi value:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("Square root of 25:", math.sqrt(25))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.9:", math.floor(4.9))

import random

print("\n--- Random Module ---")
print("Random number (1-10):", random.randint(1, 10))
print("Random number (1-100):", random.randint(1, 100))

fruits = ["mango", "banana", "apple", "grapes"]
print("Random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled fruits:", fruits)

import datetime

print("\n--- Datetime Module ---")
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)