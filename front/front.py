import streamlit as st
import json
import requests

if "guess" not in st.session_state:
    st.session_state.guess = ""
# Initialize session state for game start
if 'started' not in st.session_state:
    st.session_state.started = False
if 'widget' not in st.session_state:
    st.session_state.widget = ""
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'state' not in st.session_state:
    st.session_state.state = {}
if 'answer' not in st.session_state:
    st.session_state.answer = ""
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
    
base_url = "http://127.0.0.1:8000"

res = requests.get(f"{base_url}/title")
data = res.json()
# Display the title in Streamlit
st.text(data["title"])

def fetch_answer():
    res = requests.get(f"{base_url}/answer")
    data = res.json()
    st.session_state.state["answer"] = data["answer"]

def submit():
    if st.session_state.widget:
        st.session_state.guess = st.session_state.widget
        make_guess()

def make_guess():
    guess = st.session_state.guess
    if guess:
        inputs = {"x": guess}
        response = requests.post(url=f"{base_url}/guess", data=json.dumps(inputs))
        data = response.json()
        st.session_state.state = data.get("state", st.session_state.state)
        st.session_state.message = data["message"]
        st.subheader(st.session_state.message)

    else:
        st.error("Please enter a guess.")
        

if not st.session_state.started:
    if st.button("Start Game"):
        response = requests.post(f"{base_url}/start")
        data = response.json()
        st.session_state.state = data["state"]
        st.session_state.started = True
        st.session_state.game_over = False 
        fetch_answer()
        
        st.subheader("Game started! Good luck")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"```{st.session_state.state['print_hangman']}```")
        with col2:
            st.markdown(f"**Word to guess:** {' '.join(st.session_state.state['correctly_guessed_letters'])}")
            st.markdown(f"**Lives:** {st.session_state.state['lives']}")
else:
    if not st.session_state.game_over:
        st.text_input("Enter your guess:", max_chars=1, key="widget", on_change=submit)
        if st.button("Guess"):
            make_guess()
        else:
            st.write("Game over. Please start a new game.")

            
    # Display the current state
    if 'state' in st.session_state:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"```{st.session_state.state['print_hangman']}```")
        with col2:
            st.markdown(f"**Word to guess:** {' '.join(st.session_state.state['correctly_guessed_letters'])}")
            st.markdown(f"**Incorrectly Guessed Letters:** {' '.join(st.session_state.state['incorrectly_guessed_letters'])}")
            st.markdown(f"**Lives:** {st.session_state.state['lives']}")
            st.markdown(f"**Error Count:** {st.session_state.state['error_count']}")
            st.markdown(f"**Turn Count:** {st.session_state.state['turn_count']}")
            
            # Check if the game is over
    if st.session_state.state['lives'] < 1 or ''.join(st.session_state.state['correctly_guessed_letters']) == st.session_state.answer:
        st.markdown(f"**{st.session_state.message} 🍿🍿**")
        st.session_state.game_over = True


# To reset the game for testing purposes or when needed
if st.button("Reset Game"):
    st.session_state.started = False
    st.session_state.state = {}
    st.session_state.guess = ""
    st.session_state.widget = ""
    st.session_state.message = ""

