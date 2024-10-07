def solve_riddle(riddle):
    print(riddle)
    answer = input("Gib deine Antwort ein: ").strip().lower()
    if answer == "feuer":
        return True
    else:
        print("Das ist nicht richtig. Versuche es noch einmal.")
        return False

def end_game():
    print("Danke fürs Spielen! Auf Wiedersehen!")