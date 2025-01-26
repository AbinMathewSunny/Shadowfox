import random
import string

word_list = ['python', 'javascript', 'programming', 'computer', 'coding']

def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_hangman(attempts):
    """
    Displays the hangman figure based on the number of attempts.
    attempts: The current number of incorrect guesses.
    """
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    print(stages[attempts])

def play(word):
   
    wordcompletion = '_' * len(word) 
    guessed = set() 
    max_attempts = 6  
    attempts = 0  
    print(f"Welcome to Hangman! The word has {len(word)} letters. You have {max_attempts} attempts.")
    
    while True:
        display_hangman(attempts)
        print(f"Word: {' '.join(word_completion)}")
        
        guess = input("Guess a letter: ").upper()
        
        if len(guess) != 1 or guess not in string.ascii_letters:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed:
            print(f"You already guessed the letter {guess}.")
            continue
        
        guessed.add(guess)
        
        if guess in word:
            print(f"Correct! The letter {guess} is in the word.")
            word_as_list = list(word_completion)
            for i in [i for i, letter in enumerate(word) if letter == guess]:
                word_as_list[i] = guess
            word_completion = ''.join(word_as_list)
        else:
            print(f"Incorrect. The letter {guess} is not in the word.")
            attempts += 1
        
        if word_completion == word:
            print(f"Congratulations! You guessed the word '{word}'!")
            break
        
        if attempts == max_attempts:
            print(f"Sorry, you ran out of attempts. The word was '{word}'.")
            break
    
    play_again = input("Would you like to play again? (y/n) ").lower()
    if play_again == 'y':
        word = get_word()
        play(word)
    else:
        print("Thanks for playing!")

def main():
   
    word = get_word()
    play(word)

if __name__ == "__main__":
    main()