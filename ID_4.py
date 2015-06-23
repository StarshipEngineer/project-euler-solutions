"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse(strng):
    rev = ''
    for i in range(len(strng) - 1, -1, -1):
        rev += strng[i]
    return rev


def palindrome(number):
    num_string = str(number)
    rev_string = reverse(num_string)
    if num_string == rev_string:
        return True
    else:
        return False


pal_product = 1

span = range(999, 99, -1)

for n in span:
    for m in span:
        product = n * m
        if palindrome(product) and product > pal_product:
            pal_product = product
            factors = n, m
            print(product, "is the product of", factors)
            break
