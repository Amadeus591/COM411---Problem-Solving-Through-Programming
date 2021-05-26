print("What is your name?")
name = input()
print("Do you have a dog (type True or False)?")
dog = input()

if len(name) > 9 and dog == "True":
  print("You have a very looong name!")
  print("Your name contains {} letters.".format(len(name)))
else:
  print("Your name is quite okay!")
print("This is the end of the programm.")
