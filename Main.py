print('Welcome to hangman, try to guess the letters and find the word')
word = 'hang'
tries = 9
guess = '0'
guessed_letters = ''
while tries > 0:
    missing_letters = 4
    for char in word:
        if char in guessed_letters:
            print(char, end=' ')
            missing_letters -= 1
            if missing_letters == 0:
                print('\nYou Win!')
                print('Would you like to play again. Type yes or no')
                yes_or_no = input()
                if yes_or_no == 'yes':
                    tries = 9
                    guessed_letters = ''
                elif yes_or_no == 'no':
                    print('Goodbye')
                    quit()
        else:
            print('_', end=' ')
    print('\n\nYou have', tries, 'tries')
    guess = input('Guess a letter:\n')
    guessed_letters += guess
    tries -= 1

    if guess not in word:
        print('Wrong')
    else:
        print('Correct!')
    if tries == 0:
        print('You Lose')
        print('Would you like to play again. Type yes or no\n')
        yes_or_no = input()
        if yes_or_no == 'yes':
            tries = 9
            guessed_letters = ''
        elif yes_or_no == 'no':
            print('Goodbye')
            quit()