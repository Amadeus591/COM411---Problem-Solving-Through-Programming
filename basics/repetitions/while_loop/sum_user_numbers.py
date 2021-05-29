print("How many numbers should I sum up?")
n = int(input())
i = 1
total = 0 
while i <= n:
  print("Please enter number", i, "of", n, ":")
  x = int(input())
  i = i + 1
  total = total + x 
print("The answer is {}.".format(total))
