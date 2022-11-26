file = open ('D:\Advent_of_Code\Day3\input.txt', 'r')
file_list = []
Ones = 0
Zeros = 0
gamma = []
epsilon = []
for ele in file:
     list2 = list(ele)
     file_list.append(list2)
for i in range(0, len(file_list[0])-1):
     for ele in file_list:
        if int(ele[i]) == 0:
            Zeros+=1
        elif int(ele[i]) == 1:
            Ones+=1

     if Ones > Zeros:
         gamma.append('1')
         epsilon.append('0')
     else:
         gamma.append('0')
         epsilon.append('1')
     Zeros = 0
     Ones = 0

print (f"Nos of Zeros is {Zeros} and Nos of Ones is {Ones}")
print (''.join(gamma))
print (''.join(epsilon))
# Gamma decimal number is: 844
# Epsilon decimal number is: 3251
# Multiplication is: 2743844
file.close()