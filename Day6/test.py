with open('D:\Advent_of_Code\Day6\input.txt') as f:
    numbers = list(map(int, f.readline().strip().split(',')))


#print (numbers)

for day in range(256):
    for i in range(0, len(numbers)):
         if numbers[i] >= 1:
              numbers[i] = numbers[i] - 1
         else:
             numbers[i] = 6
             numbers.append(8)
    #print (list)

print (len(numbers))

for day in range(80, 256):
    for i in range(0, len(numbers)):
         if numbers[i] >= 1:
              numbers[i] = numbers[i] - 1
         else:
             numbers[i] = 6
             numbers.append(8)

print (len(numbers))