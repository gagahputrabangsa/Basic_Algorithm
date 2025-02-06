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


