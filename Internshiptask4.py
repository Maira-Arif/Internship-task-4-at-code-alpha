def get_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm CodeAlpha Bot!"
    elif user_input == "help":
        return "Try: hello, how are you, what is your name, bye"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


print("Chatbot started! Type 'bye' to exit.\n")

while True:
    user = input("You: ")
    reply = get_reply(user)
    print("Bot:", reply)

    if user.lower().strip() == "bye":
        break