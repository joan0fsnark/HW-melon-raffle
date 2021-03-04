"""Randomly pick customer and print customer info"""
import random
from customers import get_customers_from_file

def pick_random_customer(customers):
    winner = random.choice(customers)
    name = chosen_customer.name
    email = chosen_customer.name
    print(f"{name} at {email} has won!")

