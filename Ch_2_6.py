# Write a program to generate prime numbers with the help of a function to test prime or not.

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if(n%i) == 0:
                return False
        return True
    else:
        return False
        
def generate_prime_numbers(limit):
    primes = []
    for num in range(2,limit+1):
        if is_prime(num):
            primes.append(num)
    return primes

limit = int(input("Enter limit: "))

prime_numbers = generate_prime_numbers(limit)
print("Prime numbers up to", limit, ":",prime_numbers)

                
    
