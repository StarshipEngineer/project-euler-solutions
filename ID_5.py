"""2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def is_divisible(n, factor_span):
    divisible = True
    for i in factor_span:
        if divisible is True and n % i != 0:
            divisible = False
            break
    return divisible


max_factor = 20
factor_span = range(1, max_factor+1)
n = max_factor
answer_found = False

while answer_found == False:
    if is_divisible(n, factor_span) == False:
        n += max_factor
    else:
        answer_found = True

print(n)
