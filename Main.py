word = 'hang'
tries = 9
guess = '0'
guessed_letters = ''
correct_guesses = 0
while tries > 0:
    for char in word:
        if char in guessed_letters:
            print(char, end=' ')
        else:
            print('_', end=' ')
    print('\n\nYou have', tries, 'tries')
    guess = input('Guess a letter:\n')
    guessed_letters += guess
    if guess not in word:
        print('Wrong')
    else:
        print('Correct!')
        correct_guesses += 1
    if correct_guesses == len(word):
        print('You Win!')
        break
    tries -= 1
if tries == 0:
    print('You Lose')