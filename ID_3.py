"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


number1 = 13195
number2 = 600851475143


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


def largest_prime_factor(number):
    biggest_prime = 1
    factors = range(1, int(number / 2) + 1)
    for i in factors:
        if is_prime(i) == True and number % i == 0:
            biggest_prime = i
    return biggest_prime


a = largest_prime_factor(number2)
print(a, is_prime(a))
