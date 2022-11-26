file = open ('D:\Advent_of_Code\Day2\input.txt', 'r')
file_list = []

Depth = 0
Horizontal = 0
for ele in file:
     list2 = list(ele.split(' '))
     file_list.append(list2)

#print (file_list)
for ele in file_list:
     if ele[0] == 'down':
          Depth+=int(ele[1])
     if ele[0] == 'up':
          Depth-=int(ele[1])
     if ele[0] == 'forward':
          Horizontal+=int(ele[1])

print (Depth, Horizontal)
print ('Multiplication of Depth and Horizontal is:', Depth * Horizontal)
