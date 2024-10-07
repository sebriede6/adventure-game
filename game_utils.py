# Funktion zum Lösen des Rätsels
def solve_riddle(answer):
    global solved
    if answer.lower() == "bett":
        print("Richtig! Der Durchgang öffnet sich.")
        solved = True
    else:
        print("Falsch. Versuche es nochmal.")