#WHILE loop (and also FOR loop) can be used to have a repetition of a procedure in our code
print("How many times to print the symbol?")
x = int(input())

# i is a counter that keeps track of how many times we went through the loop
i = 0

while i < x:
  print("\u27bd", i)
  i = i + 1 # new value of the cunter is one more than it used to be

print("We left the loop.")