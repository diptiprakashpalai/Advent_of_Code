file = open ('D:\Advent_of_Code\Day1_1\input.txt', 'r')
list_file = []

count = 0
for i in file:
    list_file.append(int(i))
#print (list_file)

for i in range(0, len(list_file)-1):
    if list_file[i+1]> list_file[i]:
        count+=1

print ("No. of measurements are larger than the previous measurement is", count)

file.close()