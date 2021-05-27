print("What type of cover does the book have (soft, hard)?")
a = input()
if a == "soft":
  print("Is the book in perfect bound (yes or no)?")
  t = input()
  if t == "yes":
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coil or stiches are great for sort books.")
else:
  print("Books with hard covers can be more expensive.")
