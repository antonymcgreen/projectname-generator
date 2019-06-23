import random

windowSize=2

def learnModel(filename):
    corpus = open(filename)
    model={'^':[]}

    for word in corpus:
        word = word[:-1] + '$'
        model['^'].append(word[:windowSize])
        for i in range(len(word)-windowSize):
            window = word[i:i+windowSize]
            if window not in model:
                model[window]=[]
            model[window].append(word[i+windowSize])
    return model

def genWord(model):
    ans='^'
    while(True):
        ans+=random.choice(model[ans[-windowSize:]])
        if '$' in ans:
            return ans[1:-1]

def gen(model, length, count):
    while count>0:
        count-=1
        newWord = genWord(model)
        if len(newWord) >= length[0] and len(newWord) <= length[1]:
            print(newWord)
        else:
            count+=1

print('NAMES')
gen(learnModel('names.txt'), (5,7), 10)
print('\nCITIES')
gen(learnModel('cities.txt'), (6,8), 10)
