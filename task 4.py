"""TASK 4: Basic Chatbot
Goal: Build a simple rule-based chatbot.
Scope:
● Input from user like: "hello", "how are you", "bye".
● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
Key Concepts Used: if-elif, functions, loops, input/output.
 """
def chatbot():
        while True:
            message = input("write a text:").lower().strip()
            if message == "hello" or message == "hi":
                print("Hi!")
            elif message == "how are you?":
                print("I'm fine, thanks!")
            elif message == "bye":
                print("Goodbye!")
            else:
                print("I don't understand, human.")
chatbot()