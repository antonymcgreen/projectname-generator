import random

windowSize=3

def learnModel():
    corpus = open('cities.txt')
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


gen(learnModel(), (6,8), 10)
