import random



right_num=random.randint(1,50)
guesses=0


while guesses<5:
    user=input("Guess the right nuber between 1-50:")
    guesses += 1
    if int(user)<right_num:
     print("Higher!")
    if int(user)>right_num:
     print("Lower!")
    if int(user)==right_num:
     break

if int(user)==right_num:
    print("Congrats you chose the right number!")
elif int(user) != right_num:
    print("Sadly you didnt guess the right number, the correct number was: "+ str(right_num))
