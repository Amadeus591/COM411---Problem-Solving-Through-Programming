print("What phrase do you see?")
phrase = input()
print("\nReversing...\nThe phrase is: ", end="")
r = ""
for a in phrase:
  r = a + r
print(r)
  