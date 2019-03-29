def duplicate_encode(word):
    #your code here
    b=[]
    word = word.lower()
    for char in word:
        if word.count(char) == 1:
            b.append('(')
        else:
            b.append(')')
    result = "".join(b)  
    return result
