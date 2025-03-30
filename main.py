
import random
import time


def generate_secret_number():
    # 4-digit number, unique digits not starting with 0
    digits = list(range(1, 10))
    # first one
    first_digit = random.choice(digits)
    # last three
    digits = list(range(10)) 
    digits.remove(first_digit)
    remaining_digits = random.sample(digits, 3)
    secret_number = [first_digit] + remaining_digits
    # convert to string because input will return a string
    secret_number_str = ''.join([str(digit) for digit in secret_number])
    return secret_number_str


def is_valid_guess(guess):
    # Check 4-digits
    if len(guess) != 4:
        print("Error: Your guess must be a 4-digit number.")
        return False    
    # Check if only digits
    if not guess.isdigit():
        print("Error: Your guess must contain only digits.")
        return False  
    # Check if 0 is first
    if guess[0] == '0':
        print("Error: Your guess must not start with 0.")
        return False  
    # Check if no duplication
    if len(set(guess)) != 4:
        print("Error: Your guess must contain uonly nique digits.")
        return False
    
    return True


def evaluate_guess(guess, secret):
    bulls = 0
    cows = 0   
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1           
    return bulls, cows


def format_output(bulls, cows, start_time):
    # singular vs. plural
    bull_format = "bull" if bulls == 1 else "bulls"
    cow_format = "cow" if cows == 1 else "cows"
    run_time = time.time() - start_time
    return f"{bulls} {bull_format}, {cows} {cow_format}  (Time: {run_time:.2f} seconds)"


def game_start():
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    
    # print(f"Secret number is: {secret_number}")
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    
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

#if __name__ == "__main__":
game_start()