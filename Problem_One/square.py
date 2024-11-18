# Matthew Dingman
# Professor Qouneh

# square.py Script

# This script is used to square all numbers from 0 to 19 using a user-defined
# function called "sq()" and print them to the terminal.

# Example invocation: python3 square.py

def sq(x):
  return x * x


for x in range(20):
  num = sq(x)
  print(str(x) + " squared is equal to: " + str(num))

