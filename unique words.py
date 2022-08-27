# предполагаю, что текст уже обработан (нет знаков препинания, переноса строк, заглавных букв)

def wordProcess(txtName, encod):
    parsedText = open(txtName, encoding = encod) # кодировку, наверное можно убрать, у меня просто проблемы были
    
    uniqueWords = []
    uniqueProc = []
    onceWords = []
    onceProc = []
    
    uniqueCounter = 0
    onceCounter = 0
    wordCounter = 0
    
    words = parsedText.read().split(" ")
    for word in words:
        if not word in uniqueWords:
                uniqueWords.append(word)
                onceWords.append(word)
                uniqueCounter += 1
                uniqueProc.append(uniqueCounter)
                onceCounter += 1
                onceProc.append(onceCounter)
        else:
            uniqueProc.append(uniqueCounter)
            if word in onceWords:
                onceWords.remove(word)
                onceCounter -= 1
                onceProc.append(onceCounter)
            else: onceProc.append(onceCounter)

            wordCounter += 1
            
    parsedText.close()
    return uniqueProc, onceProc

