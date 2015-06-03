sequence = []
sequence.append(1)
sequence.append(2)
total = 2
while sequence[-1] + sequence[-2] < 4000000:
    sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1] % 2 == 0:
        total += sequence[-1]
print(total)


# for i in range(10):
#     if sequence[-1] < 100:
#         sequence.append(sequence[-1] + sequence[-2])
#         print(sequence)
#
# print(sequence)