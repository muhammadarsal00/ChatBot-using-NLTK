import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary of responses
responses = {
    'hello': 'Hi! How can I help you today?',
    'hi': 'Hello! What\'s on your mind?',
    'how are you': 'I\'m doing well, thanks! How about you?',
    'what is your name': 'My name is Chatty, nice to meet you!',
    'goodbye': 'See you later! Have a great day!',
    'thanks': 'You\'re welcome!',
    'thank you': 'You\'re welcome!',
    'bye': 'Goodbye!',
    'quit': 'Okay, see you next time!',
    'help': 'Sure, I can help you with that!',
    'what can you do': 'I can answer questions, provide information, and chat with you!',
    'tell me a joke': 'Sure, why did the chicken cross the road? To get to the other side!',
    'tell me a fact': 'Did you know that a group of flamingos is called a "flamboyance"?',
    'how old are you': 'I\'m just a computer program, I don\'t have an age!',
    'are you human': 'No, I\'m a computer program designed to simulate conversation.',
    'what time is it': 'I\'m a large language model, I don\'t have access to real-time information, but I can tell you the current time in a specific timezone if you provide it!',
    'what is the weather like': 'I\'m a large language model, I don\'t have access to real-time weather information, but I can suggest some ways for you to find out the current weather in your area!',
    'can you understand sarcasm': 'I can recognize certain patterns of sarcasm, but I may not always understand the nuances of human sarcasm.',
    'can you write a story': 'Yes, I can generate a short story for you! Do you have any specifications or prompts in mind?',
    'can you write a poem': 'Yes, I can generate a poem for you! Do you have any specifications or prompts in mind?',
    'can you translate': 'Yes, I can translate text from one language to another. Which languages would you like me to translate?',
    'can you summarize': 'Yes, I can summarize a piece of text for you. Please provide the text you\'d like me to summarize.',
    'can you give me advice': 'I can provide general advice on certain topics, but please keep in mind that I\'m just a computer program and not a professional advisor.',
    'can you play a game with me': 'Yes, I can play simple text-based games with you. What type of game would you like to play?',
    'can you recommend a book/movie/TV show': 'Yes, I can provide recommendations based on your interests. Please tell me what you\'re in the mood for!'
}


def process_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())

    # Lemmatize the tokens
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    # Join the lemmas back into a string
    input_string = ' '.join(lemmas)

    # Check if the input matches a response
    for key in responses.keys():
        if key in input_string:
            return responses[key]

    # If no match, return a default response
    return 'I didn\'t understand that. Can you please rephrase?'


def chatbot():
    print('Welcome to Chatty! I\'m here to help.')
    while True:
        user_input = input('You: ')
        response = process_input(user_input)
        print('Arsal:', response)


if __name__ == '__main__':
    chatbot()
