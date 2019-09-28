import sys

value1 = "jfj"

# write your solution here
def convert_string_to_binary(string):
    binary = ''.join('{0:08b}'.format(char, 'b') for char in bytearray(string, 'utf8'))
    return binary

print(convert_string_to_binary(value1))