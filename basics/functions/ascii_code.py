print("Program started!")
print("\nPlease enter a standard character:")
character = input()
if len(character) == 1:
  a = ord(character)
  print("The ASCII code for {} is {}.".format(character, a))
else:
  print("Character not supported!")
print("\nProgram ended!")
