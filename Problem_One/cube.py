# Matthew Dingman
# Professor Qouneh

# cube.py Script

# This script prints out the cube of all odd numbers from 0 to 19. This is done
# using the cb() user-defined function.

# Example invocation: python3 cube.py

def cb(x):
  return x * x * x

for i in range(20):
  if i % 2 != 0:
    num = cb(i)
    print("When " + str(i) + " is cubed, it becomes: " + str(num))


