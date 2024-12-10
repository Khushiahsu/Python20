#Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.

def match_words(words):
    ctr = 0
    ctr2 = []
    for a in words:
        if len(a)>1 and a[0]== a[-1]:
            ctr += 1 
            ctr2.append(a)
    print('The list of words with  first and last characters as same are \n ',ctr2)  
    return ctr
functionn = match_words(['Mango','Apple','Banana','Pear'])
print('The number having first and last characters are \n',functionn)
