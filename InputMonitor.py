import streamlit as st
import keyboard

def main():
    st.title("Input Monitor")
    st.write("Type something. Press 'Esc' to exit.")

    text_output = st.empty()
    typed_text = ""

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'esc':
                break
            elif event.name == 'enter':
                typed_text += "\n"  # Add a new line on 'Enter' key press
            else:
                typed_text += event.name
            text_output.text(typed_text)

if __name__ == "__main__":
    main()
