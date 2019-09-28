# Instructions
# You'll get two inputs, each will be a comma separated list of numbers. Each input will contain the same amount of numbers. You'll need to merge the two lists by inserting numbers from value2 into value1. Each number from value2 should be inserted such that it is placed after the next larg(est/er ?) number from value1
# Inputs

# value1
# First comma separated list of numbers

# value2
# Second comma separated list of numbers
# Sample Test Cases
# Short List
# value1 9,5
# value2 7,10
# output 9,10,5,7
# Large List
# value1 34,18,4,102
# value2 15,19,120,64
# output 34,64,18,19,4,15,102,120

def arr_merge(nums1, nums2):
    result = []
    arr1 = [int(x) for x in nums1.split(',')]
    arr2 = [int(x) for x in nums2.split(',')]
    for n in arr1:
        result.append(n)
        next_largest = min(x for x in arr2 if n < x)
        result.append(next_largest)
        arr2.remove(next_largest)
    return ','.join(str(x) for x in result)


value1 = '9,5'
value2 = '7,10'
print(arr_merge(value1, value2))

value1 = '34,18,4,102'
value2 = '15,19,120,64'
print(arr_merge(value1, value2))