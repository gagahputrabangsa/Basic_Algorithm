#this program to implement sort list using input user

num_loop = int(input('enter num of list: '))
list = [] # define the list outside the loop
for i in range (num_loop):
  iterate = 1
  num_sort = int(input(f'enter num {iterate} -> '))
  list.append(num_sort)
  iterate +=1

print(list)
  
