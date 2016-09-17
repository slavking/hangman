'''def isWordGuessed(secretWord, lettersGuessed):
    flag=True
    dictionary={}
    for i in enumerate(lettersGuessed):
        dictionary[i[1]]=i[0]
    
    for i in secretWord:
        if not (i in dictionary):
            flag=False
    return flag
'''
'''def getGuessedWord(secretWord, lettersGuessed):
    dictionary={}
    string=''
    for i in enumerate(lettersGuessed):
        dictionary[i[1]]=i[0]

    for i in secretWord:
        if i in dictionary:
            string=string+i
        else:
            string=string+'_'
    return string'''
    
def getAvailableLetters(lettersGuessed):
    import string
    strg=''
    dictionary={}
    for i in enumerate(string.ascii_lowercase):
        dictionary[i[1]]=1
    
    for i in lettersGuessed:
        if i in dictionary:
            dictionary[i]=0   
    
    for i in dictionary:
        if dictionary[i]==1:
            strg=strg+i

    list=sorted(strg)
    strg=''
    for i in list:
        strg=strg+i
        
    return strg
    

            
    
            
            
        
