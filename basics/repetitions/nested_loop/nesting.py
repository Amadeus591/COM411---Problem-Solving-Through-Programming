print("Enter the sequence.")
sequence = input()
print("Please enter the character.")
character = input()
marker1 = -1
marker2 = -1
for a in range(0, len(sequence), 1):
  b = sequence[a]
  if b == character:
    if (marker1 == -1): 
      marker1 = a
    else:
      marker2 = a
print(f"The distance between the marker is {marker2 - marker1 -1}.")