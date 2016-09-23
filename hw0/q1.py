import sys

index = int(sys.argv[1])
filename = sys.argv[2]

column = []
file = open("hw0_data.dat", "r")

for line in file.readlines():
    row = line.strip().split(' ')
    column.append(float(row[index]))

column.sort()
result = ','.join(str(element) for element in column)

open('ans1.txt', 'w').write(result)