# Matthew Dingman
# Professor Qouneh

# computeFunction.py Script

# This script computes value for the function f(x) = x^2 + x for x = 0 to 9.

# Example Invocation: python3 computeFunction.py

nums = []
for x in range(10):
  print("When x = " + str(x))
  y = x^2 + x
  print("F(x) = " + str(y))


