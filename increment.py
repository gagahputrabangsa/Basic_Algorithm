import keyboard
counter = 1
while True:
  
  inputs = (input(f'This is counter number-> {counter}'))
  #apply increment method
  counter += 1
  if keyboard.is_pressed('q'):  # Exit loop on q key
    print('Thanks!')
    break
