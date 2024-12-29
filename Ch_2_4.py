# Write a program to sort the array elements using bubble sort technique.

def bubbleSort(arr):
    n = len(arr) #mistake
    for i in range(n-1): #mistake (n-1) constant 
        for j in range(0,n-i-1): #mistake (0,n-i-1) is not constant 9,8,7....
            if arr[j] > arr[j+1]: #mistake
                arr[j],arr[j+1] = arr[j+1], arr[j]


arr = [23,5,32,6,83,4,35,44,0]
bubbleSort(arr)
print("Sorted array list: ")
for i in arr: #mistake
    print(i, end=" ");
