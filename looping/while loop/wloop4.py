import time

def countdown(n):
  """
  This function performs a countdown from n to 1, pausing for 1 second at each number.
  """
  while n > 0:
    print(n)
    n -= 1
    time.sleep(1)
def print_triangle_pattern(height):
  """
  This function prints a right-angled triangle pattern with the specified height.
  """
  i = 1
  while i <= height:
    j = 1
    while j <= i:
      print("*", end="")
      j += 1
    print()
    i += 1



def main():
  """
  The main function of the program.
  """
  print("Starting countdown from 10:")
  countdown(10)


  print("\nPrinting a right-angled triangle pattern:")
  print_triangle_pattern(7)

  print("\nFinished.")

if __name__ == "__main__":
  main()
