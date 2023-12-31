# BIG KEYS - N-Gram Text Editor
## Overview
BIG KEYS developed using Flask and implements an n-gram language model to enhance your typing experience!
The program uses the NLTK (Natural Language Toolkit) database along with the text you type into the text editor to increase its prediction abilities. 
BIG KEYS gets more powerful the more you use it-- as the program learns how you type, it gets better an better at completing your sentences. 

## How It's Made
BIG KEYS is developed using the Flask web framework, incorporating the TinyMCE library for the editor interface and the SweetAlert library for notifications. Text data is stored and retrieve with the use of the Pickle library.

##Features
N-Gram Language Model: BIG KEYS employs an N-gram language model to analyze previous text and predict how to complete the sentence.

NLTK Database: The program leverages the NLTK database to access a rich source of linguistic data, improving the accuracy and diversity of predictions.


##How to Use
Installation:

Ensure you have Python installed on your system.
Install the necessary dependencies by running:
bash
Copy code
pip install flask tinyMCE sweetalert pickle
Run the Program:

Clone the BIG KEYS repository to your local machine.
Navigate to the project directory and run the following command:
bash
Copy code
python big_keys.py

##Typing with Predictive Text:

To complete your sentence, select the personal or general sentence completion buttons in the header of the text editor. Using data that you have put into the text editor, or data from the NLTK database, BIG KEYS will complete your sentence. 

##Dependencies
Python
Flask
TinyMCE
SweetAlert
Pickle

##Contributing
If you'd like to contribute to BIG KEYS, feel free to fork the repository, make your changes, and submit a pull request. We welcome contributions to improve the functionality and performance of the program.

##License
This project is licensed under the MIT License, which means you are free to use, modify, and distribute the software. See the LICENSE file for more details.

##Acknowledgments
BIG KEYS acknowledges the contributions of the NLTK project and the open-source community for providing valuable linguistic data and tools.
