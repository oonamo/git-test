import math

print("hello, world!")

def median(input):
    input_len = len(input)
    mid = math.floor(input_len / 2)

    if input_len % 2 == 1:
        return input[mid]

    return (input[mid] + input[mid - 1]) / 2

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))
