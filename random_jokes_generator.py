import streamlit as st
import pyjokes

def main():
    st.title("Random Joke Generator")
    
    joke_button = st.button("Generate Joke")
    
    if joke_button:
        joke = pyjokes.get_joke()
        st.write(joke)

if __name__ == "__main__":
    main()
