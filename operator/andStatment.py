#age recognition

age = 56

#if statement using AND operator to determine the criteria from the 'age' variable
if age <= 5:
  print('baby')
elif age > 5 and age < 12:
  print('kid')
elif age > 12 and age < 21:
  print('adolescent')
elif age > 21 and age < 40:
  print('adult')
elif age > 40:
  print('Old')
