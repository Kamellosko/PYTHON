lucky_numbers = [4,6,1,82,14]
friends = ["Denis","Dawidek","Grubasek","Kolejny","Pan"]
friends.extend(lucky_numbers)
friends.append("Boniek")
friends.insert(1, "Tede")
friends.remove("Dawidek")

print(friends)

print("\n")

###not working print(friends.index("Dawidek"))

friends[0] = "Benis"
print(friends[0])
print("\n")
print(friends[-2])
print("\n")
print(friends[1:4])

