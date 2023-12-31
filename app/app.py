import re
from flask import Flask, render_template, request, url_for, jsonify
from Processing.TriesAndDict.Dictionary import Dictionary
import Processing.TriesAndDict.TriNode as TriNode
from Processing.TriesAndDict.TextGeneration import TextGenerator
import Processing.TriesAndDict.Words as Words 

app = Flask(__name__)


generator = TextGenerator()
generator.obtainData()





previousName = ""

def updatePrev(name):
    previousName = name



@app.route('/')
def index(): 

    return render_template('index.html')
    

save_name = None

@app.route('/names', methods=['GET', 'POST'])
def passWords():
    
    if request.method == "POST":
        
        name = request.get_json()
        name = re.sub("<.*?>", "", name)
        name = re.sub("&nbsp;", "", name)

        if previousName in name:
            name.replace(previousName, "")



        words = name.split()[-4:]


        context = ()
        word = ""
        if 0 < len(words) < 4:
            
            for i in range(len(words) - 1):
                context += (words[i],)

            context = ("",) * (4 - len(words)) + context

            value = words[-1]

            generator.appendDictionary(context, value)

        elif len(words) == 4:

            for i in range(3):
                context += (words[i],)
    
            value = words[-1]

            generator.appendDictionary(context, value)

        
        generator.appendDictionaryWithLine(name)

       
        updatePrev(name)

        print(generator.personalGenerator)
        
        return jsonify(name)
    
    
    return url_for(input())


@app.route('/handle_data', methods=['POST'])
def handle_data():

    text_data = request.get_json()
    method = request.get_json()[0]
    text_data = request.get_json()[1] 

    text_data = re.sub("<.*?>", "", text_data)
    text_data = re.sub("&nbsp;", "", text_data)
    print(text_data)
    if method == "Submit":

        words = text_data.split()[-3:]

        context = ()
        update = ""
        if 0 < len(words) < 3:
            for i in range(len(words)):
                context += (words[i],)

            context = ("",) * (3 - len(words)) + context


            update = generator.mostCommonCompleteSentence(context)

        elif len(words) == 3:
            for i in range(3):
                context += (words[i],)
            
            update = generator.mostCommonCompleteSentence(context)


    

        text_data = update
    elif method == "Submit1":


        words = text_data.split()[-3:]


        context = ()
        update = ""
        if 0 < len(words) < 3:
            for i in range(len(words)):
                context += (words[i],)

            context = ("",) * (3 - len(words)) + context


            update = generator.generateSentence(context)

        elif len(words) == 3:
            for i in range(3):
                context += (words[i],)
            
            update = generator.generateSentence(context)
        
        text_data = update

        
    
    elif method == "Submit2":


        words = text_data.split()[-3:]


        context = ()
        update = ""
        if 0 < len(words) < 3:
            for i in range(len(words)):
                context += (words[i],)

            context = ("",) * (3 - len(words)) + context


            update = generator.completeSentence(context)

        elif len(words) == 3:
            for i in range(3):
                context += (words[i],)
            
            update = generator.completeSentence(context)
        
        text_data = update 
        



        
    print(text_data)

    return jsonify(text_data)
    # return render_template('index.html', text_data=text_data)


if __name__ == "__main__":
    app.run(debug=False)



