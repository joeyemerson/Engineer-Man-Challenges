import sys
import re

value1 = 'doggo:chase\" \"name:em\"}'

# write your solution here
def fix_json(string):
    
    # Fix inner contents between quotes
    result = re.sub('{?\"?([^{\"]+)\"?:\"?([^}\"]+)\"?,?}?', '\"\\1\":\"\\2\"', string)
    # Ensure separate items are separated by comma
    result = re.sub('\"\,?\s*,?\"', '\",\"', result)
    # Ensure beginning of string contains brace
    result = re.sub('^{?', '{', result)
    # Ensure end of string contains brace
    result = re.sub('}?$', '}', result)

    return result


print(fix_json(value1))