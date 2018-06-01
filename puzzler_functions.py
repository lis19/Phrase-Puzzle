"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    
    return puzzle == view


def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if puzzle is the same as view or if
    current_selection is 'QUIT'.
    
    >>> game_over('kale', 'kale', 'CONSONANT')
    True
    >>>game_over('orange', 'ora^^e', 'VOWEL')
    False
    """
    
    return puzzle == view or current_selection == QUIT


def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if letter is in puzzle and letter not in view.
    
    >>> bonus_letter('lettuce', 'l^^tu^e', 'c')
    True
    >>> bonus_letter('kiwi', 'ki^i', 'i')
    False
    """
    
    return letter in puzzle and letter not in view
    
    
def update_letter_view(puzzle: str, view: str, index: int, guess: str) -> str:
    """Return guess if guess is the character at index of puzzle. Otherwise,
    return the character at that index of view.
    
    >>> update_letter_view('cucumber', 'cuc^^b^r', 3, 'u')
    u
    >>> update_letter_view('pizza', 'pi^^a', 2, 'k')
    ^
    """
    
    if guess == puzzle[index]:
        return puzzle[index]
    else:
        return view[index]
    

def calculate_score(current_score: int, letter_occurrences: int, \
    letter_type: str) -> int:
    """Return the new score by calculating it in terms of the current score.
    
    >>> calculate_score(7, 2, 'CONSONANT')
    9
    >>>calculate_score(5, 3, 'VOWEL')
    4
    """
    
    if letter_type == CONSONANT:
        return current_score + letter_occurrences * CONSONANT_POINTS
    else:
        return current_score - VOWEL_PRICE


def next_player(current_player: str, occurrences: int) -> str:
    """Return the next player for the game depending on number of occurrences.
    
    Precondition: occurrences >= 0.
    
    >>> next_player(PLAYER_ONE, 3)
    'Player One'
    >>> next_player(PLAYER_ONE, 0)
    'Player Two'
    """

    player_to_go = ''
    
    #will switch players
    if occurrences > 0:
        if current_player == PLAYER_ONE:
            player_to_go = PLAYER_ONE
        else:
            player_to_go = PLAYER_TWO
      
    #will keep the same player  
    elif occurrences == 0:
        if current_player == PLAYER_ONE:
            player_to_go = PLAYER_TWO
        else:
            player_to_go = PLAYER_ONE  
            
    return player_to_go
