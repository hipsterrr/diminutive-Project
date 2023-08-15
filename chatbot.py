import streamlit as st

# Define a dictionary with some predefined responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
}

def get_response(input_text):
    input_text = input_text.lower()
    response = responses.get(input_text, "I'm sorry, I don't understand.")
    return response

def main():
    st.title("Simple Chatbot")

    user_input = st.text_input("You: ", "")
    if st.button("Send"):
        response = get_response(user_input)
        st.text("Bot: " + response)

if __name__ == "__main__":
    main()
