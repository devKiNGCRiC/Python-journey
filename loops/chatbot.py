while True:
    message = input("You: ")

    if message.lower() in ['hi', 'hello']:
        print("AI: Hello! How can i help you?")
    elif 'time' in message.lower():
        print("AI: I can't tell time yet, but I'm learning!")
    elif message.lower() == 'bye':
        print("AI: GOODBYE!")
        break
    else:
        print("AI: I don't understand, but i'm trying!")