print("Program started!")
print("\nPlease enter an ASCII code:")
code = int(input())
if code in range(32, 127):
  print(f"\nThe character represented by the ASCII code {code} is {chr(code)}")
else:
  print("This is not an ASCII code!")
print("\nProgram Ended!")
