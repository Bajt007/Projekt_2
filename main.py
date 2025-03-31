
import random
import time

def generate_secret_number() -> str:
    """
    Generates a secret 4-digit number with unique digits, not starting with 0
    Returns:
        str: Generated secret number as a string
    """
    digits = list(range(1, 10))
    # first digit
    first_digit = random.choice(digits)
    # last three digita
    digits = list(range(10)) 
    digits.remove(first_digit)
    remaining_digits = random.sample(digits, 3)
    secret_number = [first_digit] + remaining_digits
    # convert to string because input will return a string
    secret_number_str = ''.join([str(digit) for digit in secret_number])
    return secret_number_str

def is_valid_guess(guess: str) -> bool:
    """
    Checks if the given guess is a valid 4-digit number
    Arg:
        guess (str): User's guess as a string
    Returns:
        bool: True if the guess is valid, otherwise False
    """
    error = []
    # Check 4-digits
    if len(guess) != 4:
        error.append(f"Error: Your guess must be a 4-digit number, you entered {len(guess)} digits.") 
    # Check if only digits
    if not guess.isdigit():
        error.append(f"Error: Your guess must contain only digits, you entered '{guess}'.")
    # Check if 0 is first
    if guess[0] == '0':
        error.append("Error: Your guess must not start with 0.")
    # Check if no duplication
    if len(set(guess)) != 4:
        error.append("Error: Your guess must contain uonly nique digits.")
    if error:
         for e in error:
            print(e)
         return False
    return True

def evaluate_guess(guess: str, secret: str) -> tuple:
    """
    Evaluates user's guess against the secret number, calculates bulls and cows
    Args:
        guess (str): The user's guess
        secret (str): The secret number
    Returns:
        tuple: A tuple containing the number of bulls and cows
    """
    bulls = 0
    cows = 0   
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1           
    return bulls, cows

def format_output(bulls: int, cows: int, start_time: float) -> str:
    """
    Formating the output string to display the number of bulls, cows and the time
    Args:
        bulls (int): amount of bulls.
        cows (int): amount of cows.
        start_time (float): The starting time of the game
    Returns:
        str: a formatted string displaying the bulls, cows and time
    """
    # singular vs. plural
    bull_format = "bull" if bulls == 1 else "bulls"
    cow_format = "cow" if cows == 1 else "cows"
    run_time = time.time() - start_time
    return f"{bulls} {bull_format}, {cows} {cow_format}  (Time: {run_time:.2f} seconds)"

def game_start():
    """
    Starts the game Bulls and Cows, handling user inputs, calculates elapsed time, evaluates results and outputs
    """
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    
    # print(f"Secret number is: {secret_number}")
    print("""
    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    """)
    
    while True:
        if attempts == 0:
            guess = input("Enter a number: ")
        else:
            guess = input(">>> ")
      
        if not is_valid_guess(guess):
            continue
        
        attempts += 1
        bulls, cows = evaluate_guess(guess, secret_number)
        
        if bulls == 4:
            run_time = time.time() - start_time
            print(f"Correct, you've guessed the right number")
            print(f"in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            print("-----------------------------------------------")
            print(f"{"That's amazing! - You are really awesome!"  if attempts == 1 else"That's amazing!"}!")
            print(f"Total time: {run_time:.2f} seconds")
            break
        else:
            print(format_output(bulls, cows, start_time))
            print("-----------------------------------------------")

if __name__ == "__main__":
    game_start()