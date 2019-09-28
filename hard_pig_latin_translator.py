
# Instructions
# Your input variable will contain a sentence/phrase in pig latin. Your job is to translate it to english. You add "yay" if the word starts with a vowel. Otherwise move the starting consonant sequence (w, wr, sch, ...) to the end of the word and add "ay" plus a dash.
# Inputs
# value1
# Sentence/phrase in pig latin.
# Sample Test Cases
# Short phrase
# value1 ayay imple-say est-tay ase-cay
# output a simple test case
# Long phrase
# value1 ig-pay atin-lay isyay usedyay inyay ools-schay o-tay each-tay anguage-lay onstructs-cay
# output pig latin is used in schools to teach language constructs

def trans_pig(phrase):
    result = []
    words = [w for w in phrase.split()]
    for word in words:
        if '-' in word:
            parts = word.split('-')
            result.append(parts[1].replace('ay', '') + parts[0])
        else:
            result.append(word.replace('yay', ''))
    return ' '.join(result)

print(trans_pig('ayay imple-say est-tay ase-cay'))
print(trans_pig('ig-pay atin-lay isyay usedyay inyay ools-schay o-tay each-tay anguage-lay'))