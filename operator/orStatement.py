#this's simple implementation of an OR operator using if statement
q = input('What gender are you? (Male/Female) ')

if q == 'Male' or q== 'male': 
  print('You are Male')

elif q == 'Male' or q== 'female': #this Or statement will choose either you input Female or female, it will still running correctly 
  print('You are Female')
