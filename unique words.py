#!/usr/bin/env python
# coding: utf-8

# In[114]:

# added comment
# предполагаю, что текст уже обработан (нет знаков препинания, переноса строк, заглавных букв)

def wordProcess(txtName, encod):
    parsedText = open(txtName, encoding = encod)
    
    uniqueWords = []
    uniqueProc = []
    onceWords = []
    onceProc = []
    
    uniqueCounter = 0
    onceCounter = 0
    wordCounter = 0
    
    temp = ""
    
    for symb in parsedText.read() + " ": # тут костыль с добавлением пробела, чтобы последнее слово записывалось в массив
        if symb != " ":
            temp = temp + symb
        else:
            if not temp in uniqueWords:
                uniqueWords.append(temp)
                onceWords.append(temp)
                uniqueCounter += 1
                uniqueProc.append(uniqueCounter)
                onceCounter += 1
                onceProc.append(onceCounter)
            else:
                uniqueProc.append(uniqueCounter)
                if temp in onceWords:
                    onceWords.remove(temp)
                    onceCounter -= 1
                    onceProc.append(onceCounter)
                    
            wordCounter += 1
            temp = ""
    parsedText.close()
    return uniqueProc, onceProc


# In[116]:


uP, oP = wordProcess("D:\Learning\chapters1-9\chapter1.txt", "utf8")
print(uP, "\n"*5, oP)

