#!/usr/bin/env python

userInput = input("Enter a list of numbers between 1 and 100 , separated by spaces: ")
nums = userInput.split()
for num in nums:
  if not num.isdigit():
    print("Not a number", num)
  elif int(num) < 1:
    print("Number is less than 1 ",num )
  elif int(num) > 100:
    print("Number is greater than 100, ", num)
  else:
    print("Number is valid ", num)
