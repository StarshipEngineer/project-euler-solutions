# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# maybe tackle this from the other end- multiply primes until the product matches the input
# This is because the number can be so huge



number1 = 13195

def is_prime(number):
    if number > 2:    
        i = 0
        prime = True
        for i in range(2, number):
            remainder = number % i
            if remainder == 0:
                prime = False
                break  
        return prime
    if number <= 2 and number >= 0:
        return True

def biggest_prime_factor(number):
    biggest_prime = 1
    for i in range (2, int(number / 2)):
        if is_prime(i) == True:
            biggest_prime = i
    return biggest_prime

# Still doesn't work

a = biggest_prime_factor(number1)
print(a)
