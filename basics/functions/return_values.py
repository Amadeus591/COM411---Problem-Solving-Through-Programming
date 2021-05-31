def sum_weights(a, b):
  s = a + b
  return s

def calc_avg_weight(a, b):
  avg = (a + b) / 2
  return avg

def run():
  print("Please enter the weight of Beep:")
  a = float(input())
  print("Please enter the weight of Bop:")
  b = float(input())
  print("Please enter sum or average:")
  x = input()
  if (x == "sum"):
    answer = sum_weights(a, b)
    print("The sum of Beep's and Bop's weight is {}.".format(answer))
  elif (x == "average"):
    answer = calc_avg_weight(a, b)
    print("The average of Beep's and Bop's weight is {}".format(answer))
  else:
    print("I am not sure what you want to do!")

run()


