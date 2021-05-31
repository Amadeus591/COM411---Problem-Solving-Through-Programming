print("Please enter a value.")
h = float(input())
print("Please enter the second value.")
b = float(input())
# Defining my own funtion to calculate the area of a triangle.
def calculate_area(h, b):
  area = 0.5 * h * b
  print("The area of this triangle is {}".format(area))
# Call for the function
print()
calculate_area(h, b)


# Parameter is a value that you plug into a function.
