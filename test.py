import wordSuggest
"""
ToDo: 
1) error catch for if double letter, one green, one grey
2) change input style so no spaces?
"""

MyFile=open("words.txt","r")
content=MyFile.read()
# print(content)
WL=content.split("\n")
MyFile.close()
WL=WL[:-1]
#print(WL)
AL=['their', 'price']
LL=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(LL)
def letterCount(WL, LL):
    L=[0]*26

    for i in WL:
        #print('--------')
        #print(i)
        for l in i:
            count=0
            #print('-----')
            #print(l)
            for a in LL:
                #print('---')
                #print(a)
                #print(count)
                if l==a:
                    L[count]=L[count]+1
                    #print('if made: ' + str(L[count]))
                count=count+1
    #count=0
    #for i in L:
        #print(LL[count] + ': ' + str(i))
        #count=count+1
                      
    res=dict(zip(LL, L))
    sortRes={}
    sorted_keys=sorted(res, key=res.get, reverse=True)

    for w in sorted_keys:
        sortRes[w]=res[w]
    return sortRes

#L=[0]*26
#for i in WL:
    #print('--------')
    #print(i)
    #print(i[0])
    #count=0
    #for a in LL:
        #if i[0]==a:
            #L[count]=L[count]+1
        #count=count+1
#count=0
#for i in L:
    #print(LL[count] + ': ' + str(i))
    #count=count+1

#print("Letter Counts:")
#print(letterCount(WL, LL))
#print(letterCount(WL,LL).keys())
#print('-------------------')

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
                    if str(i[l]) == str(letters[a]) and l != a:
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
        

wordle = True
rnd=1
wordleList = WL
while wordle == True:
    print("I suggest you try: " + str(wordSuggest.wordSuggest(wordleList)))
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
        #print(wordleList)
        
    print("Which letters were green? (Type \"none\" if none)")
    correctLetters=input()
    if correctLetters!="none":
        correctLetters=inputCorrection(correctLetters,guess)
        #([*correctLetters])
        #print(correctLetters)
        wordleList = wordFilter(wordleList,correctLetters,2)
        #print(wordleList)
        #print(letterCount(wordleList,LL))
        
    print("Which letters are yellow? (Type \"none\" if none)")
    yellowLetters=input()
    if yellowLetters!="none":
        yellowLetters = inputCorrection(yellowLetters,guess)
        #print(yellowLetters)
        wordleList = wordFilter(wordleList,yellowLetters,3)
        #print(wordleList)
        #print(letterCount(wordleList,LL))

    rnd+=1
    if rnd==6:
        wordle = False
