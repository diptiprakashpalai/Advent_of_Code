file = ['Down 5', 'Down 2', 'Up 3', 'Forward 3', 'Forward 4']
file_list = []
Depth = 0
Horizontal = 0
for ele in file:
     list2 = list(ele.split(' '))
     file_list.append(list2)

print (file_list)
for ele in file_list:
     if ele[0] == 'Down':
          Depth+=int(ele[1])
     if ele[0] == 'Up':
          Depth-=int(ele[1])
     if ele[0] == 'Forward':
          Horizontal+=int(ele[1])

print (Depth, Horizontal)
print ('Multiplication of Depth and Horizontal is:', Depth * Horizontal)
