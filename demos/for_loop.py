#Product that displays a menu and allows a user to either see a nice message, calculate the area of a rectangle, calculate the area of a triangle, or display a times table for a number.

option = 1
while (option != 9):

  print("\nPlease choose an option from the menu:\n")
  print("1 - See a nice message.\n2 - Calculate the are of a rectangle.\n3 - Calculate the area of a triangle.\n4 - See a times table for a number.\n9 - Exit!")

  option = int(input())

  if option == 1:
    print("\nToday is going to be a nice day!")
  elif option == 2:
    print("\nPlease enter the length of the rectangle:")
    l = int(input())
    print("\nPlease enter the width of the rectangle:")
    w = int(input())
    area = l*w
    print("\nThe area of this rectangle is {}.".format(area))
  elif option == 3:
    print("\nPlease enter the base of the triangle:")
    b = float(input())
    print("\nPlease enter the height of the triangle:")
    h = float(input())
    area = 0.5*b*h
    print("\nThe area of this triangle is {:.2f}".format(area))
  elif option == 4:
    print("\nWhat number would you like to see the times table for?")
    n = int(input())
    for i in range (1,11,1):
      print("{}x{} = {}".format(n, i, n*i))
 