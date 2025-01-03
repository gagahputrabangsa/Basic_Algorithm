#this program to implement sort list using input user

num_loop = int(input('enter num of list: '))
list = [] # define the list outside the loop
for i in range (num_loop):
  iterate = 1

  num_sort = int(input(f'enter num {num_loop} -> '))
  list.append(num_sort)
  num_sort +=1

print(list)
  
