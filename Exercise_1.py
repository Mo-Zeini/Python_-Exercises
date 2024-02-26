# Exercise 1 (and Solution)

'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).
'''

import datetime

name = input("Please, enter your name: ")
age = float(input("Please, enter your age: "))

current_date = datetime.date.today()
current_year = current_date.year

print("current year is: ", current_year)

turn_year = 100 - int(age)

turn_100 = turn_year + current_year

print(f"In {turn_100}, you will be 100 years old")

