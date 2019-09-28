# calculate mode of all integers in string

value1 = "1,4,5,67,9,23,4,5,4"

# write your solution here
# print number that appears most

def frequent_num(string):
    arr = string.split(',')
    counter = {}
    for item in arr:
        counter[item] = counter.get(item, 0) + 1
    winner = max(counter, key=counter.get)
    return winner

print(frequent_num(value1))