try:
    import TriNode
except:
    import Processing.TriesAndDict.TriNode as TriNode

class Dictionary:
    def __init__(self):
        self.dict = {}

    def __str__(self) -> str:
        return  str(self.dict)
    
    def addWord(self, word):
        TriNode.insert(self.dict, word)
    
    def checkWord(self, word):
        return TriNode.contains(self.dict, word)

    def defaultDictionary(self):
        fileNames = ["TriesAndDict/texts/HarryPotter.txt", "TriesAndDict/texts/HowToCreateAMind.txt", "TriesAndDict/texts/Kafka.txt", "TriesAndDict/texts/PercyJackson.txt", "TriesAndDict/texts/two_cities.txt"]

        for file in fileNames:
            TriNode.addText(self.dict, file)


    


