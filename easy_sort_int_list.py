value1 = '1,4,7,-4,88,102,-1234'

# write your solution here
def sort_list(integers):
    return ','.join(sorted(integers.split(','), key=int, reverse=True))

print(sort_list(value1))
