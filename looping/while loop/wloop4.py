import time

def countdown(n):
  """
  This function performs a countdown from n to 1, pausing for 1 second at each number.
  """
  while n > 0:
    print(n)
    n -= 1
    time.sleep(1)


