print("What level of brightness is required?")
level = int(input())
print("\nAdjusting brightness...")
for a in range (2, level + 1, 2):
  print("\nBeep's brighnesss level:{}".format("*" * a),"\nBop's brighness level:{}".format("*" * a))
print("\nAdjustments complete.")
