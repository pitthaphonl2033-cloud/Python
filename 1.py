pattern=[12,23,34,45]
pattern.append(56)
print(pattern)

pattern=[12,23,34,45]
pattern.insert(2,56)
print(pattern)

pattern=[12,23,34,45]
pattern.extend([56,67,78,89,90])
print(pattern)

pattern=[12,23,34,45]
pattern.append([56,67,78,89,90])
print(pattern)

pattern=[12,23,34,45]
pattern.remove(23)
print(pattern)

pattern=[12,23,34,45]
pattern.pop(3)
print(pattern)

pattern=[12,23,34,45]
pattern.clear()
print(pattern)

pattern=[12,23,34,45]
del pattern[0]
print(pattern)

sports=["football","basketball","badminton","volleyball","cricket"]
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports.append("tennis")
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
sports.append(sports2)
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
sports.insert(2,"golf")
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
sports3=["bowling","dodgeball","baseball","pickleball","futsal"]
sports.extend(sports3)
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
sports3=["bowling","dodgeball","baseball","pickleball","futsal"]
sports.extend(sports3)
sports.remove("pickleball")
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
sports.pop(1)
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
del sports[0]
print(sports)

sports=["football","basketball","badminton","volleyball","cricket"]
sports2=input("Enter sports name")
sports.clear()
print(sports)
