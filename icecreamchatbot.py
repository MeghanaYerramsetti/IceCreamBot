def get_response(user_input):
    user_input = user_input.lower()  # Normalize the input to lowercase
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to our ice cream parlor! How can I help you today?"
    elif "flavors" in user_input:
        return "We have chocolate, vanilla, strawberry, and mint. Which one would you like to try?"
    elif "size" in user_input:
        return "We offer small, medium, and large sizes. What size would you like?"
    elif "order" in user_input:
        return "Great! Please tell me your flavor and size."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Enjoy your ice cream!"
    elif "bye" in user_input:
        return "Goodbye! Have a sweet day!"
    else:
        return "I'm sorry, I didn't understand that. Can I help you with flavors, sizes, or placing an order?"

# Main loop to interact with the user
def chat():
    print("Welcome to the Ice Cream Parlor Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(get_response(user_input))
            break
        response = get_response(user_input)
        print("Bot:", response)

# Start the chat
if __name__ == "__main__":
    chat()
