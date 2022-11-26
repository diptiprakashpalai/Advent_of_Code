file = open ('D:\Advent_of_Code\Day3\input.txt', 'r')
file_list = []

Ones = 0
Zeros = 0

for ele in file:
     list2 = list(ele)
     file_list.append(list2)

result = file_list
print (len(file_list))
#print (file_list[0])

for i in range(0, len(file_list[0])-1):
     for ele in file_list:
        if int((ele[i])) == 1:
            Ones+=1
        elif int((ele[i])) == 0:
            Zeros+=1
     if (Ones > Zeros) or (Ones == Zeros):
         for ele in file_list:  
            if int((ele[i])) == 1:
                file_list.remove(ele)
            #print (file_list)
            #print ('--------------------')
     elif Ones < Zeros:
         for ele in file_list:         
            if int((ele[i])) == 0:
                file_list.remove(ele)
            #print (file_list)
            #print ('---------------------')
                
     Ones = 0
     Zeros = 0


          
print (file_list)  
file.close() 
