import random
#lista
people = [...]

presence = {}

while len(people) != 0:
    winnerName = random.choice(people)
    people.remove(winnerName)
    answer = input(f"Czy {winnerName} jest obecny?")
    presence[winnerName] = answer
    #print(winnerName)
    #print(people)
    #input("Press enter to continue")

presence_count = 0
absences_count = 0

for person in presence.key():
    print(f"{person} say that is {presence[person]}")
    # Y \ N
    if presence[person] == "Y":
        presence_count = presence_count + 1
    else:
        absences_count = absences_count + 1    
        
print(f"Osoby obecne : {presence_count}")
print(f"Osoby nieobecne : {len(people) - presence_count}")
