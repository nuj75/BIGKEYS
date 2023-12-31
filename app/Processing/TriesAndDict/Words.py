import re
import random
from nltk.corpus import twitter_samples, gutenberg
from nltk.tokenize import word_tokenize








def append_dictionary(file_name, k, d):
    file = open(file_name, "r")
    context = ("",) * k
    
    for line in file:
        for word in line.split(" "):
            word = word.strip("\n\t ")
            if not(word.isnumeric()):
                associate_pair(d, context, word)
                context = context[1:] + (word,)
            
                
    for i in range(k):
        associate_pair(d, context, "") 
        context = context[1:] + (word,)

def input_append_dictionary(input, k, d):

    context = ("",) * k

    input = input.replace("\n", " ")
    input = input.replace("\t", " ")
    
    for word in input.split(" "):
        
        if not(word.isnumeric()):
            associate_pair(d, context, word)
            context = context[1:] + (word,)
                
    for i in range(k):
        associate_pair(d, context, "") 
        context = context[1:] + ("",)

def associate_pair(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]


def corpus_dictionary(k):
    d = {}
    context = ("",) * k
    for file in gutenberg.fileids():
        for word in gutenberg.raw(file).split(" "):
            
            word = word.replace("\n", " ")
            word = word.replace("\t", " ")
            
            while "*" in word:
                word = word.replace("*", "")

            word = re.sub("<.*?>", "", word)
            word = re.sub("&nbsp;", "", word)

            associate_pair(d, context, word)
            context = context[1:] + (word,)

            associate_pair(d, context, "")
        
        for file in twitter_samples.fileids():
            for word in twitter_samples.raw(file):
               word = word.replace("\n", " ")
            word = word.replace("\t", " ")
            
            while "*" in word:
                word = word.replace("*", "")

            word = re.sub("<.*?>", "", word)
            word = re.sub("&nbsp;", "", word)

            associate_pair(d, context, word)
            context = context[1:] + (word,)

            associate_pair(d, context, "") 
        
    
    return d



    


def completeSentence(d, context, k):
    
    text = ""
    
    i = 0

    

    while i < 100 and not ("." in text or "!" in text or "?" in text) and not(context == ("", "", "")):
        


        followWords = d[context]

        try:
            followWords.remove("")
            
        except:
            pass



        if followWords == []:
            followWords.append("")


        word = max(set(followWords), key=followWords.count)

        if context[2] != "" and context[2][-1] == ".":
            word[0] = word[0].upper()

        
        text += word + " "

        context = context[1:] + (word,)
        
        i += 1
    
    return text.strip()

def generateSentence(d, context, k):


    text = ""

    
    while not ("." in text or "!" in text or "?" in text) and not(context == ("", "", "")):
        followWords = d[context]
        

        try:
            while "" in followWords:
                followWords.remove("")
            
        except:
            pass



        if followWords == []:
            followWords.append("")

        word = followWords[random.randint(0, len(followWords) - 1)]


        if word != "":
            text += word + " "

        context = context[1:] + (word,)
    
       

       
    
    return text
