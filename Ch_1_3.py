byte_array = bytearray([10,20,30,40,50])

print("Original byte array elements:")
for i in byte_array:
    print(i,end=' ')
print()

byte_array[1] = 45
byte_array[4] = 75

print("Modified byte array elements:")
for i in byte_array:
    print(i,end=' ')

