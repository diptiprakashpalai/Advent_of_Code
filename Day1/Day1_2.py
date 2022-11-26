file = open ('D:\Advent_of_Code\Day1_1\input2.txt', 'r')
list_file = []
list_file1 = []
measurement = []

ln = 0
result = 0
count = 0
# Get the list of the input
for i in file:
    list_file.append(int(i))

print (len(list_file))
# Iterate for length of input
for k in range(0, len(list_file)-1):
     # Iterate until sum of 3 elements is possible
     if len(list_file) > (k+1)+1:
        # Make list of 3 elements for sum
         for i in range(ln, ln+3):
             list_file1.append(list_file[i])
         result = sum(list_file1)
         ln+=1
         measurement.append(result)
         result = 0
         list_file1.clear()

print (len(measurement))
# Check which 3 elemnts sum is greater than previous one
for i in range(0, len(measurement)-1):
    if measurement[i+1]> measurement[i]:
        count+=1
print (count)
file.close()