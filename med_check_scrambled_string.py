import sys

value1 = 'brian,airbx'

# write your solution here
def check_string(string):
    dict1 = {}
    dict2 = {}
    arr = string.split(',')

    # create dictionaries for each string to count characters
    # if character counts match, the second is a permutation
    for char in arr[0]:
        dict1[char] = dict1.get(char, 0) + 1
    for char in arr[1]:
        dict2[char] = dict2.get(char, 0) + 1

    result = dict1 == dict2
    return "Yes" if result == True else "No"


print(check_string(value1))