ChatBot-using-NLTK<br>
It is the Repository to automatically gives answers to your questions.<br>
Below is a brief summary of the chatbot script: 
Import Libraries:
nltk: Natural Language Toolkit used to process text.
word_tokenize: Function called to break text apart into individual words.
WordNetLemmatizer: Tool used to return words into their root forms. 
Set Up Components:
lemmatizer: A WordNetLemmatizer object used for lemmatization.
Build Responses:
responses: A dictionary that connects specific user inputs to pre-set inputs to provide chatbot responses.
process_input function:  
Break Input: This will take the input string from the user and break it into words and make each word lower case. 
Find root words: Changes words into their base form.
Look for a match: This matches the users return to the dictionary responses and returns the appropriate answer. 
Default answer: Returns a default answer if none was found. 
chatbot function:
Say hello: Looks up and prints a welcome message corresponding to the user. 
Keep talking: Once it has the above working, everytime the user does something (i.e. types), it repeat steps 2-4 above. 
Launch the script:
The if statement is a condition that tells at what point the chatbot() function to run the script. 
This script produces a rudimentary text-based chatbot that responds to supposed user inputs regarding everyday "chit chat" topics. It uses tokenization and lemmatizes or transforms user inputs to link inputs to the appropriate responses. 
