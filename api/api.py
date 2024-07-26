from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils.game import Hangman


class User_input(BaseModel) : 
    x :str 
    
app = FastAPI()
game = Hangman()

@app.post("/start") 
def start() : 
    game.reset_game()
    return {"message": "Game started", "state": game.display_game_status(True, None), "title" : game.title}
    

@app.post("/guess")
def guess(user_input : User_input) : 
    try : 
        guess =  game.get_guess(user_input.x)
    except ValueError as e : 
        raise HTTPException(status_code=400, detail=str(e))

    flag = guess not in game.wrongly_guessed_letter and guess not in game.correctly_guessed_letters
    if not flag : 
        return {"message": "You already submitted this letter!", "state": game.display_game_status(flag, guess)}
    
    game.update_game_state(guess)
    
    if game.well_played():
        return {"message": f"You found the word: {''.join(game.word_to_find)} in {game.turn_count} turns with {game.error_count} errors!", "state": game.display_game_status(flag, guess)}
    elif game.game_over():
        return {"message": f"You lose, the word was {''.join(game.word_to_find)}", "state": game.display_game_status(flag, guess)}
    else:
        return {"message": "Keep guessing!", "state": game.display_game_status(flag, guess)}


@app.get("/title")
def get_title(): 
    return {"title" : game.title}


@app.get("/answer")
def get_answer() : 
    return {"answer" : "".join(game.word_to_find)}

    
