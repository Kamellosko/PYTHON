secret_word="gigachad"
guess=""
guess_count=0
guess_liimt=3
out_of_guess= False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_liimt:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You lost!")
else:  
    print("You guessed right!")    