from typing import Dict, List

def insert(data :Dict, word :str):
    if word == "":
        data[""] = [True, {}]
    elif len(word) == 1:
        if word in data:
            data[word][0] = True
        else:
            data[word] = [True, {}]
    elif word[0] in data:
        insert(data[word[0]][1], word[1:])
    else:
        data[word[0]] = [False, {}]
        insert(data[word[0]][1], word[1:])

def addText(dict, fileName):
    file = open(fileName, "r")

    for line in file:
        words = line.split(" ")
        
        
        for word in words:
            word = word.strip("!@#$%^&*()_+-={}|:\";'<>?,./)\n!-1234567890[].").lower()

            try:
                insert(dict, word)
            except:
                pass
    

            
    
        

def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.
    """
    total = 0

    #base case: data has no values in it, will never enter the loop, returns 0
    #recursive case: data has values in it. If the value itself corresponds to a word
    #                then add a 1, else, recursion call to the values connected to the node
    
    for val in data.values():
        if val[0] == True:
            total += 1
        
        total += count_words (val[1])
    
    return total





def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.
    """

    #base case: if the length of the string is 0 or 1, then check if it is a key in data. 
    #           if isn't, then return False. Otherwise, return whether the trie says its a word. 
    #           If the word is an empty string, return True.
    if len(s) < 2:
        return s == "" or (s in data and data[s][0] == True)
    


    #recursive case: if the first character of the strign is in the trie, then 
    #                do a recursive call using the dictionary associated with it, 
    #                and shrink the string by taking out the first char
    
    currChar = s[0]

    if currChar in data:
        return contains(data[currChar][1], s[1:])
    

    #base case: the char in the string isn't in the trie and 
    #           therefore can't possibly be in the trie
    return False 
    
                     


    

def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.
    """
    #base case: prefix is nothing. You just want to find all the words in inputted trie
    if prefix == "":
        #second recursion problem: return all the words in a trie
        return findAllWords(data)
    
    #recursive case: call the function again but on the tail. 
    #                when the base case is reached, and the words are put into the list
    #                then bubble back up, adding the first letter to each thing in the list

    elif prefix[0] in data:
        head = prefix[0]
        tail = prefix[1:]
        return addToList(get_suggestions(data[head][1], tail), head)
    
    #base case: if the head isn't in data, then there are no solutions
    else: 
        return []

#HELPER FUNCTION FOR F5
def findAllWords(data):

    #base case: dictionary is empty. Return empty list
    if data == {}:
        return []
    

    words = []
    
    #loop through every key. 
    for key in data.keys():
        #Base Case: if the key is True, then it is the final node after
        #           a successful word. add it to word

        if data[key][0] == True:
            words.append(key)

        #recursive case: if the key corresponds to a false and isn't
        #                empty, recurse on the dictionary corresponding to the key
        #                when the function bubbles up, then the keys will be
        #                added to each word in the list.

        if not data[key][1] == {}:
            words = words + addToList(findAllWords(data[key][0]), key)


        #Base Case: The prefix is both empty and doesn't correspond to a True
        #           Therefore, this branch doesn't correspond to a word.
        #           It won't be added to the list.   
    return words

#HELPER FUNCTION FOR F5 and findAllWords
def addToList(list, letter):
    returnVal = []

    #add the letter to the beginning of each word.
    #importantly, if the list is empty, then nothing will happen
    #findAllWords --> this means that is the second base case is reached
    #                 then there will be nothing in the list, and so nothing in added for the branch. 
    #F5 --> if the second base case is reached, nothing will populate in the list.  
    for word in list:
        returnVal.append(letter + word)
    
    return returnVal
  