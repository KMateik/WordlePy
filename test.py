import wordSuggest
"""
ToDo: 
1) error catch for if double letter, one green, one grey
"""

MyFile=open("words.txt","r")
content=MyFile.read()
# print(content)
WL=content.split("\n")
MyFile.close()
WL=WL[:-1]
#print(WL)

def wordFilter(wordleList, letters, n):
    filteredList = []
    if n == 1:
        #print("grey letters:" + str(letters))
        for i in wordleList: #step through words
            addWord=True
            #print(i)
            for l in i: #step through letters of each word
                for a in letters: #compare letters in word to letters given
                    #print(l + " : " + a)
                    if l == a:
                        #print("if triggered")
                        addWord=False
                        break
                if addWord==False:
                    break
            if addWord == True:
                filteredList.append(i)
    if n == 2: # Green letters
        #print("green letters:" + str(letters))
        letterCount=0
        for i in letters:
            if i != ' ':
                letterCount+=1
        #print(letterCount)
        for i in wordleList: #step through words
            addWord=0
            letterC=0
            c=1
            #print(i)
            for l in range(len(i)): #step through letters of each word
                for a in range(len(letters)): #compare letters in word to letters given
                    if str(i[l]) == str(letters[a]) and l != a:
                        #print("bad if triggered")
                        addWord=2
                        #break

                    if str(i[l]) == str(letters[a]) and l == a:
                        #print("good if triggered")
                        letterC+=1
                        #break
                    if letterC == letterCount:
                        addWord=1
                    a+=1
                #if addWord==1:
                    #print("Word Added")
                    #break
                #if addWord==2:
                    #break
                l+=1
            if addWord == 1:
                filteredList.append(i)
    if n == 3: # yellow letters
        #print("yellow letters:" + str(letters))
        letterCount=0
        for i in letters:
            if i != ' ':
                letterCount+=1
        #print(letterCount)
        for i in wordleList: #step through words
            addWord=0
            letterC=0
            c=1
            #print(i)
            for l in range(len(i)): #step through letters of each word
                for a in range(len(letters)): #compare letters in word to letters given
                    #if i == "array":
                        #print(str(i[l]) + "::" + str(letters[a]) + str(l) + ":" + str(a))
                    if str(i[l]) == str(letters[a]) and l != a:
                        letterC+=1
                        #break
                        #if i == "array":
                            #print(str(letterC) + " = " + str(letterCount))
                    if letterC == letterCount:
                        
                        addWord=1
                    if str(i[l]) == str(letters[a]) and l == a:
                        addWord=0
                        letterC-=1
                    a+=1
                    #if i == "array":
                        #print(addWord)
                #if addWord==1:
                    #print("Word Added")
                    #break
                #if addWord==2:
                    #break
                l+=1
            if addWord == 1:
                filteredList.append(i)
                for x in letters:
                    if x != ' ':
                        if x not in i:
                            filteredList.remove(i)
                            break
                
    if n == 4:
        #print("green letters:" + str(letters))
        for i in wordleList: #step through words
            addWord=True
            #print(i)
            for l in i: #step through letters of each word
                for a in letters: #compare letters in word to letters given
                    #print(l + " : " + a)
                    if l == a:
                        #print("if triggered")
                        addWord=False
                        break
                if addWord==False:
                    break
            if addWord == True:
                filteredList.append(i)
    return filteredList

def inputCorrection(UserIn, Guess):
    #pass
    #print(UserIn + ' : ' + Guess)
    if len(UserIn) != 5:
        Correction = [' '] * 5
        for i in UserIn:
            #print("****")
            #print(i)
            for a in range(0,5):
                #print("a= " + str(a))
                if i == Guess[a]:
                    Correction[a] = i
        return Correction
    else:
        return UserIn
        

wordle = True
rnd=0
wordleList = WL
wordSugL = WL
correctLetters = None

while wordle == True:
    SW = wordSuggest.wordSuggest(wordleList, wordSugL, correctLetters)
    if len(SW) == 3:
        a = 1
        narrowIn = []
        for w in SW:
            b = 0
            for l in w:
                #print(l + "=" + SW[a][b])
                if l != SW[a][b] and a == 1:
                    narrowIn.append(l)
                elif l != SW[a][b] and a == 2:
                    narrowIn.append(l)
                    narrowIn.append(SW[a][b])
                b+=1
            a+=1
            if a == 3:
                print(narrowIn)
                SW = []
                for w in WL:
                    if narrowIn[0] in w and narrowIn[1] in w and narrowIn[2] in w:
                        SW.append(w)
                break

    print("I suggest you try: " + str(SW))
    print("Did you guess the word right? (y/n)")
    gameOn = input()
    if gameOn == 'y':
        wordle = False
        break
    print("What word did you try?")
    guess=input()

    print("Which letters were grey? (Type \"none\" if none)")
    greyLetters=input()
    if greyLetters!="none":
        greyLetters=inputCorrection(greyLetters,guess)
        #([*greyLetters])
        #print(greyLetters)
        wordleList = wordFilter(wordleList,greyLetters,1)
        if rnd == 0:
            wordSugL = wordleList
        else:
            wordSugL = wordFilter(wordSugL, greyLetters, 1)
        #print(wordleList)
        
    print("Which letters are yellow? (Type \"none\" if none)")
    yellowLetters=input()
    if yellowLetters!="none":
        yellowLetters = inputCorrection(yellowLetters,guess)
        #print(yellowLetters)
        wordleList = wordFilter(wordleList,yellowLetters,3)
        if rnd == 0:
            wordSugL = wordleList
        else:
            wordSugL = wordFilter(wordSugL, yellowLetters, 3)
        #print(wordleList)

    print("Which letters were green? (Type \"none\" if none)")
    correctLetters=input()
    if correctLetters!="none":
        correctLetters=inputCorrection(correctLetters,guess)
        #([*correctLetters])
        #print(correctLetters)
        wordleList = wordFilter(wordleList,correctLetters,2)
        wordSugL = wordFilter(wordSugL,correctLetters,1)
        #wordSugL = wordFilter(wordSugL,correctLetters,4)
        #print(wordleList)
        #print("*-*-*")
        #print(wordSugL)

    rnd+=1
    if rnd==6:
        wordle = False
        break
