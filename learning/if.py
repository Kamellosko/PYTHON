is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male or tall or both ")
elif is_male and not(is_tall):
    print("You are a male and also you are a small human being")
elif not(is_male) and not(is_tall):
    print("Tall woman")

else:
    print("You are not a male nor tall :(")

print("\n")

if is_male and is_tall:
    print("You are a tall male ")
else:
    print("You are not a male or you are not tall :(")