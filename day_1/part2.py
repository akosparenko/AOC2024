with open('./day_1/input.txt', 'r') as file:
    # Unpack columns directly
    array1, array2 = zip(*[map(int, line.split()) for line in file])

# Convert to integers if needed
array1 = [int(x) for x in array1]
array2 = [int(x) for x in array2]

count_dict = {}
for num in array2:
    count_dict[num] = count_dict.get(num, 0) + 1
    
    
total = 0
for num in array1:
    if num in count_dict.keys():
        total += num*count_dict[num]
        
print(total)