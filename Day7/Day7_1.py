with open('D:\Advent_of_Code\Day7\input.txt') as f:
    numbers = list(map(int, f.readline().strip().split(',')))

#print (numbers)
Total_list = []
for i in range(506):
    Total = 0
    for number in numbers:
        number= number - i
        Total = Total + number
    Total_list.append(Total)

print (len(Total_list))
print (min(Total_list))
f.close()
