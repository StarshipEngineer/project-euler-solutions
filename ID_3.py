# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 13195
highest_prime = 1

for i in range(1, number):
    if number % i == 0:
        for n in range(1, i):
            if i % n != 0:
                highest_prime = i

print(highest_prime)


# highest_prime_factor = 1
# divisor = int(number / 2)
#
# while divisor > 0:
#
#     divisor -= 1
#
#
#     divisor_is_prime = True
#     if number % divisor == 0:
#         for factor_divisor in range(1, divisor):
#             if divisor % factor_divisor == 0:
#                 divisor_is_prime = False
#                 divisor += 1
#             else:
#                 highest_prime_factor = divisor
#     divisor += 1
#
# print(highest_prime_factor)
# #
# # for divisor in range(1, number):
# #     if number % divisor == 0:
# #         for factor_divisor in range(1, divisor):
# #             if divisor % factor_divisor == 0:
# #                 outer_is_prime = False
# #                 break
# #             else:
# #                 outer_is_prime = True
# #     if outer_is_prime is not False:
# #         highest_prime_factor = divisor # Problem! It's just printing outer, no matter what
