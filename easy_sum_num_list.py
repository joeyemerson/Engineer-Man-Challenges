value1 = "1,2,44,5,333"

# write your solution here
def sum_num_list(string):
    return sum(int(x) for x in string.split(','))

print(sum_num_list(value1))