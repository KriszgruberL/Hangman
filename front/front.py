import streamlit as st
import json
import requests

# Initialize session state variables
if "guess" not in st.session_state:
    st.session_state.guess = ""
if "started" not in st.session_state:
    st.session_state.started = False
if "widget" not in st.session_state:
    st.session_state.widget = ""
if "message" not in st.session_state:
    st.session_state.message = "Game started! Good luck"
if "state" not in st.session_state:
    st.session_state.state = {}
if "answer" not in st.session_state:
    st.session_state.answer = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "title_displayed" not in st.session_state:
    st.session_state.title_displayed = False
    

base_url = "http://127.0.0.1:8000"


def print_title(rerun=False):
    """
    Prints the title of the game.

    Parameters:
    - rerun (bool): If True, reruns the function to display the title again.

    Returns:
    None
    """
    if not st.session_state.title_displayed:
        if not rerun: 
            # Fetch the title from the server
            res = requests.get(f"{base_url}/title")
            data = res.json()
            # Display the title in Streamlit
            st.text(data["title"])
            st.session_state.title_displayed = True
        else :
            # Rerun the function to display the title again
            st.rerun()

def fetch_answer():
    """
    Fetches the answer from the server and stores it in the session state.

    Returns:
    None
    """
    # Fetch the answer from the server
    res = requests.get(f"{base_url}/answer")
    data = res.json()
    # Store the answer in the session state
    st.session_state.state["answer"] = data["answer"]


def submit():
    """
    Submits the user's guess and calls the make_guess function.

    Returns:
    None
    """
    # Check if the widget has a value
    if st.session_state.widget:
        # Set the guess to the value of the widget
        st.session_state.guess = st.session_state.widget
        # Call the make_guess function
        make_guess()


def make_guess():
    """
    Makes a guess based on the user's input.

    Returns:
    None
    """
    guess = st.session_state.guess  # Get the user's guess from the session state
    if guess:
        if not st.session_state.game_over:
            if len(guess) == 1 and guess.isalpha() : 
                inputs = {"x": guess}  # Create a dictionary with the guess as the value
                response = requests.post(url=f"{base_url}/guess", data=json.dumps(inputs))  # Send a POST request with the guess data
                data = response.json()  # Parse the response as JSON
                st.session_state.state = data.get("state", st.session_state.state)  # Update the session state with the new game state
                st.session_state.message = data["message"]  # Update the session state with the new message
                st.subheader(st.session_state.message)  # Display the message as a subheader
                # st.session_state.guess = ""  # Clear the guess from the session state
                # st.session_state.widget = ""  # Clear the widget from the session state
            # Check if the game is over
                if st.session_state.state['lives'] < 1 or ''.join(st.session_state.state['correctly_guessed_letters']) == st.session_state.answer:
                    st.session_state.game_over = True

                st.session_state.widget = ""  # Clear the input field
            else : 
                st.error("Please enter a single letter.")
        else:
            st.write("Game over. Please start a new game.")
            reset_game()
    else:
        st.error("Please enter a guess.")

def display_state():
    """
    Displays the current state of the game.

    Returns:
    None
    """
    # Check if "state" key exists in st.session_state
    if "state" in st.session_state:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"```{st.session_state.state['print_hangman']}```")

        with col2:
            st.markdown(
                f"**Word to guess:** {' '.join(st.session_state.state['correctly_guessed_letters'])}"
            )
            st.markdown(
                f"**Incorrectly Guessed Letters:** {' '.join(st.session_state.state['incorrectly_guessed_letters'])}"
            )
            st.markdown(f"**Lives:** {st.session_state.state['lives']}")
            st.markdown(f"**Error Count:** {st.session_state.state['error_count']}")
            st.markdown(f"**Turn Count:** {st.session_state.state['turn_count']}")

def start_game():
    """
    Starts a new game.

    This function sends a POST request to the base URL to start a new game. It updates the session state with the game state,
    sets the 'started' and 'game_over' flags, fetches the answer, and clears the title display. Finally, it reruns the script.

    Returns:
    None
    """
    # Send a POST request to start a new game
    response = requests.post(f"{base_url}/start")
    data = response.json()

    # Update session state with game state
    st.session_state.state = data["state"]

    # Set flags for game status
    st.session_state.started = True
    st.session_state.game_over = False
    
    fetch_answer()

    # Clear the title when the game starts
    st.session_state.title_displayed = False
    st.rerun()


def reset_game():
    """
    Resets the game for testing purposes or when needed.

    Returns:
    None
    """
    st.session_state.started = False
    st.session_state.state = {}
    st.session_state.guess = ""
    st.session_state.widget = ""
    st.session_state.message = ""
    # Reset the title display state
    st.session_state.title_displayed = False
    st.rerun()




# Check if the game has not started yet
if not st.session_state.started:
    # Display the title if it hasn't been displayed yet
    print_title()

    start_game_button = st.button("Start Game")
    if start_game_button:
        start_game()

    reset_game_button = st.button("Reset Game")
    if reset_game_button:
        reset_game()
else:
    display_state()

    if not st.session_state.game_over:
        st.text_input("Enter your guess:", max_chars=1, key="widget", on_change=submit)
        if st.button("Guess"):
            make_guess()
    else:
        st.write("Game over. Please start a new game.")
    
    if st.session_state.game_over:
        reset_game_button = st.button("Reset Game")
        if reset_game_button:
            reset_game()

    if st.session_state.state.get('lives', 1) < 1 or ''.join(st.session_state.state.get('correctly_guessed_letters', [])) == st.session_state.answer:
        st.session_state.game_over = True
        st.session_state.widget = ""
        st.session_state.guess = ""

