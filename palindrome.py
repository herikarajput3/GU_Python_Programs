num = int(input("Enter number to check whether it is palindrome or not:"))
temp = num

def isPalindrome(num):
    rev = 0
    while(num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    return rev

palin = isPalindrome(temp)

if(temp == palin):
    print("The number is a palindrome")
else:
    print(f"{temp} is not a palindrome")
    
