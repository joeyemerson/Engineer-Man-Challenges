import sys

#starting number in sequence
value1 = '21'

#calculate value2 digits of sequence
value2 = '40'

# write your solution here
def fib(x,y):
    fib_sequence = ''
    counter = 0
    a, b = 0, 1
    while counter < y:
        if a == x:
            fib_sequence += f'{b}'
            counter += 1
        if fib_sequence != '' and a != x:
            fib_sequence += f',{b}'
            counter += 1
        a, b = b, a + b
    return fib_sequence

print(fib(int(value1), int(value2)))