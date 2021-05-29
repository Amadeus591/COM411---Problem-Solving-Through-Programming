print("What strange markings do you see?")
markings = input()
print("\nIdentifying...")
for a in range (0, len(markings), 1):
  print("index", a, ":", markings[a])
