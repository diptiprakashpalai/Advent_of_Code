file = open ('D:\Advent_of_Code\Day2\input.txt', 'r')
file_list = []
Aim = 0
Depth = 0
Horizontal = 0
for ele in file:
     list2 = list(ele.split(' '))
     file_list.append(list2)

#print (file_list)
for ele in file_list:
     if ele[0] == 'forward':
          Horizontal+=int(ele[1])
          Depth = Depth + Aim * int(ele[1])
     elif ele[0] == 'down':
          Aim+=int(ele[1])
     elif ele[0] == 'up':
          Aim-=int(ele[1])
     

print ('Depth is:{} & Horizontal is: {}'.format(Depth, Horizontal))
print ('Multiplication of Depth and Horizontal is:', Depth * Horizontal)
file.close()
