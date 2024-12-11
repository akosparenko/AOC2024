with open('./day_1/input.txt', 'r') as file:
    # Unpack columns directly
    array1, array2 = zip(*[map(int, line.split()) for line in file])

# Convert to integers if needed
array1 = [int(x) for x in array1]
array2 = [int(x) for x in array2]

array1.sort()
array2.sort()

totalDistance = 0

for index in range(len(array1)):
    totalDistance += abs(array1[index] - array2[index])

print(totalDistance)

