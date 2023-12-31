try:
    import Words
except:
    import Processing.TriesAndDict.Words as Words

import pickle
import json

class TextGenerator:
    def __init__(self):
        self.generator = {}
        self.personalGenerator = {}


        
    def obtainData(self):
        # try:
        with open("app/Processing/TriesAndDict/generator.pickle", "rb") as file:   
            # self.generator = Words.corpus_dictionary(3)
            self.generator = pickle.load(file)
            # pickle.dump(self.generator, file)
        with open("app/Processing/TriesAndDict/personalGenerator.pickle", "rb") as file:
            self.personalGenerator = pickle.load(file)
           
        # except: 
            # pass
        

    def dumpData(self):
        self.generator = Words.corpus_dictionary(3)

        fileNames = ["app/Processing/TriesAndDict/texts/HarryPotter.txt", "app/Processing/TriesAndDict/texts/HowToCreateAMind.txt", "app/Processing/TriesAndDict/texts/Kafka.txt", "app/Processing/TriesAndDict/texts/PercyJackson.txt", "app/Processing/TriesAndDict/texts/two_cities.txt", "app/Processing/TriesAndDict/texts/Kafka.txt", "app/Processing/TriesAndDict/texts/PercyJackson.txt", "app/Processing/TriesAndDict/texts/two_cities.txt", "app/Processing/TriesAndDict/texts/LordOfTheFlies.txt"]

        for file in fileNames:
            Words.append_dictionary(file, 3, self.generator) 
        
        with open("app/Processing/TriesAndDict/generator.pickle", "wb") as file:
            pickle.dump(self.generator, file)

            
    def updatePersonal(self):
        with open("app/Processing/TriesAndDict/personalGenerator.pickle", "wb") as file:
            pickle.dump(self.personalGenerator, file)

        
    
        


    
    def generateSentence(self, context):
        text = ""
        
        if context in self.generator:
            
            text = Words.generateSentence(self.generator, context, 3)
            return text
        return text
    
    def mostCommonCompleteSentence(self, context):
        text = ""

        if context in self.personalGenerator:
            text = Words.completeSentence(self.personalGenerator, context, 3)
            return text
        return text
    
    def completeSentence(self, context):
        text = ""


        if context in self.personalGenerator:

            text = Words.completeSentence(self.personalGenerator, context, 3)
            return text
        

        return text

    def appendDictionary(self, context, word):
        if context in self.personalGenerator:
            self.personalGenerator[context].append(word)
        else:
            self.personalGenerator[context] = [word]
        
        with open("app/Processing/TriesAndDict/personalGenerator.pickle", "wb") as file:
            pickle.dump(self.personalGenerator, file)

    
    def appendDictionaryWithLine(self, input):
        Words.input_append_dictionary(input, 3, self.personalGenerator)

        with open("app/Processing/TriesAndDict/personalGenerator.pickle", "wb") as file:
            pickle.dump(self.personalGenerator, file)

        


    


