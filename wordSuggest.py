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

def wordSuggest(WSL):
    LC = letterCount(WSL,LL)
    #print(LC)
    x = list(LC.keys())
    #print(x)
    count=0
    L=[0]*len(WSL)
    for i in WSL: #word
        #print("***********")
        #print(i)
        
        for l in i: #letter
            #print(l)
            for a in range(0,5):
                #print("-----------")
                #print(x[a])
                if l == x[a]:
                    #print(count)
                    L[count]=L[count]+1
        count+=1
    #print(L)
    res=dict(zip(WSL,L))
    #print(res)
    sortRes={}
    sorted_keys=sorted(res, key=res.get, reverse=True)

    for w in sorted_keys:
        sortRes[w]=res[w]
    #print(sortRes)
    j = list(sortRes.keys())

    if len(j) >= 3:
        wordSug=['']*3
        for w in range(0,3):
            wordSug[w] = j[w]
    else:
        wordSug = j
    return wordSug
LL=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = ["light", "maybe", "right", "their", "drain", "ready", "other", "where", "years", "place", "sound", "while", "above"]

#print(wordSuggest(words))
