import google.generativeai as genai

# The SDK will use the API key from your environment variables
model = genai.GenerativeModel('gemini-1.5-flash')

# This starts a chat session that will store conversation history
chat = model.start_chat(history=[])

print("🤖 Gemini Chatbot is ready! Type 'exit' or 'quit' to end the chat.")
print("-" * 30)

# This loop will run forever until you type exit or quit
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    # Send your message to the chat and get a response
    response = chat.send_message(user_input)
    print(f"Bot: {response.text}\n")