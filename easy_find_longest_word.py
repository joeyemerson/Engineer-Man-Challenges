# Instructions
# You'll get one input, a string with multiple words. Return the longest word in the string. If the input contains multiple words that are the largest length, return a string that contains all of the words in the same order they are provided. All returned strings should be lowercase and trimmed of whitespace.
# Inputs

# value1
# Single string with multiple words.
# Sample Test Cases
# Regular
# value1 run,barn,yellow,barracuda,shark,fish,swim
# output barracuda
# Same Size
# value1 fishes,sam,gollum,sauron,frodo,balrog
# output fishes,gollum,sauron,balrog


def find_longest_word(s):
    result = []
    words = s.split(',')
    max_length = len(max(words, key=len))
    for word in words:
        if len(word) == max_length:
            result.append(word)
    return ','.join(result)



print(find_longest_word('run,barn,yellow,barracuda,shark,fish,swim'), 'barracuda')
print(find_longest_word('fishes,sam,gollum,sauron,frodo,balrog'), 'fishes,gollum,sauron,balrog')