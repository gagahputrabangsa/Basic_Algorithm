#this program implements a sorted list using input user but in reverse
num_loop = int(input('enter num of list: '))

list = [] # define the list outside the loop
iterate = 1 #give an iteration
for i in range (num_loop):
  num_sort = int(input(f'enter num {iterate} -> '))
  list.append(num_sort) #append the num to list
  iterate +=1 #use incursive to the iterate var

print('List ->',list) #unsorted or Original list
#in order to reverse a sorted list, we need to sort the list first
sorted = sorted(list) #we'll make a var to store the sorted list
print('Reversed List ->',sorted[::-1]) #this will reverse the sorted list
  
