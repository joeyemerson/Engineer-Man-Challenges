# This function takes in a string and converts
# to roman numeral value.

NUMERALS = {'M': 1000, 'CM': 900,
            'D': 500, 'CD': 400,
            'C': 100, 'XC': 90,
            'L': 50, 'XL': 40,
            'X': 10, 'IX': 9,
            'V': 5, 'IV': 4,
            'I': 1}

def convert_rn(string):
    result = 0
    for i in range(len(string)):
        try:
            result += NUMERALS[string[i:i+2]]
            i += 2
        except:
            result += NUMERALS[string[i]]
            i += 1
    return result

value1 = input('Enter roman numerals to calculate:\n')

# checks for valid roman numerals, but is incomplete.
# currently only filters strings with no characters
# in the 'values' dict and any non-string value
try:
    print(convert_rn(value1))
except:
    print('You did not enter valid roman numerals. Try again.')