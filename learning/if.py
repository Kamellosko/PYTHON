is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male or tall or both ")
elif is_male and not(is_tall):
    print("You are a male and also you are a small human being")
elif not(is_male) and (is_tall):
    print("You are tall woman")
else:
    print("You are small woman")

print("\n")

if is_male or is_tall:
    print("You are a male or you are just tall ")
else:
    print("You are not a male or you are not tall :(")