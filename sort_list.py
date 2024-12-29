#list1 = [64, 34, 25, 12, 22, 11, 90]
list1 = [int(input("Enter a list of numbers: "))]
print("Original list:", list1)

def sort(list):
    n = 7
    temp = 0
    i = 0
    while (i < n):
        j = 0
        while (j < n - i - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
            j++
        i++

sort(list1)
print("Sorted list:", list1)
