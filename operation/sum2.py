while True:
  try:
    first_num = int(input('enter your first num: '))
    second_num = int(input('enter your second num: '))
    
    result = first_num + second_num
    print(f"{first_num} + {second_num} = {result} ") #formatting result
  
    asking = input ('wanna continue? (Y/N)').lower() #lowercase all the user input
    if asking == 'n':
      break    
except ValueError:
  print('Invalid input. Please enter integers only.')
