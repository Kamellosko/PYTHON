from itertools import count


lucky_numbers = [4,6,1,82,14]
friends = ["Denis","Dawidek","Grubasek","Kolejny","Pan","Pan"]
friends.extend(lucky_numbers)
friends.append("Boniek")
friends.insert(1, "Tede")
friends.remove("Dawidek")

print(friends)
print("\n")

print(friends.index("Grubasek"))
print("\n")

friends[0] = "Benis"

print(friends[0])
print("\n")

print(friends[-2])
print("\n")

print(friends[1:4])
print("\n")

print("Numbers of Pan\'s")
print(friends.count("Pan"))
print("\n")

lucky_numbers.sort()
print(lucky_numbers)
print("\n")

lucky_numbers.reverse()
print(lucky_numbers)
print("\n")

friends2= friends.copy()
 
print(friends2)
print("\n")