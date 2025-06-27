print("hello, world!")

def mean(input):
    sum = 0
    for index in input:
        sum += index
    return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))
