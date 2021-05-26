print("What is your name?")
name = input()
# print("Do you have a dog (type True or False)?")
# dog = input()

if len(name) >= 9:
  print("You have a very looong name!")
  print("Your name contains {} letters.".format(len(name)))
elif len(name) > 6:
  print("Your name is a bit long. Consider a nickname.")
elif len(name) < 3:
  print("Your name is veeery short!")
else:
  print("Your name is quite okay!")
print("This is the end of the programm.")

