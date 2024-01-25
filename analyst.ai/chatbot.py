import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name",
        ["I am a simple chatbot.",]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) your name",
        ["I am a simple chatbot.",]
    ],
    [
        r"what can you do",
        ["I can answer basic questions and engage in a conversation.",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day.",]
    ],
]

# Create a chatbot using the pairs defined above
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Start the chat
if __name__ == "__main__":
    start_chat()
