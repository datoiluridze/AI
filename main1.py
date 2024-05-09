import random

class SimpleAI:
    def __init__(self):
        self.responses = {
            "hello": ["Hello!", "Hi there!", "Hey!"],
            "how are you": ["I'm good, thanks!", "Feeling great!", "Pretty good!"],
            "bye": ["Goodbye!", "See you later!", "Bye!"]
        }

    def respond(self, message):
        message = message.lower()
        for key in self.responses:
            if key in message:
                return random.choice(self.responses[key])
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    ai = SimpleAI()
    print("AI: Sup, yo im your AI. How can I help you")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break
        response = ai.respond(user_input)
        print("AI:", response)
