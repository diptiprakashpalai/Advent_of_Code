file = open ('D:\Advent_of_Code\Day3\input.txt', 'r')
file_list = []
result = []

Ones = 0
Zeros = 0
count = 0
count1 = 0

for ele in file:
     list2 = list(ele)
     file_list.append(list2)
     count+=1

print (len(file_list))
print (count)

for ele in file_list:
    if int((ele[0])) == 1:
        print ("1 at the begining")
        print (ele)
        Ones+=1
for ele in file_list:
    if int((ele[0])) == 0:
        print ("0 at the begining")
        print (ele)
        Zeros+=1
print ('Ones: {}, Zeros: {}'.format(Ones, Zeros))

for ele in file_list:         
     if int((ele[0])) == 1:
        count1+=1
        #print (ele)
        #print (count1)
        file_list.remove(ele)
        result.append(ele)
        

#print (result)
print (len(file_list))
print (len(result))