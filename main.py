import game_utils

print("Willkommen im adventuregame: Die verlorene Schatzsuche")
name = input("Bitte gib deinen Namen ein: ")
def greeting(name):
 print(f"Hallo, {name}!")
greeting(name)

import random

# Räume und ihre Beschreibungen
rooms = {
    "Start": "Du befindest dich in einem dunklen Raum. Ein schwaches Licht dringt durch eine Spalte in der Tür.",
    "Raum1": "Ein kleiner Raum mit einem Tisch und einem Buch darauf.",
    "Schatzkammer": "Du hast die Schatzkammer erreicht! Ein glänzender Schatz liegt auf einem Podest."
}

# Gegenstände und ihre Beschreibungen
items = {
    "Buch": "Ein altes, verstaubtes Buch mit seltsamen Symbolen."
}

# Rätsel und Lösung
riddle = "Was hat einen Kopf, aber keinen Körper, einen Fuß, aber keinen Schuh? Ein Bett."
solved = False

# Aktueller Raum und Inventar
current_room = "Start"
inventory = []

# Funktion zum Anzeigen des aktuellen Raums und Inventars
def look_around():
    print(rooms[current_room])
    if items in current_room:
        print("Du siehst:", ", ".join(items))

# Funktion zum Bewegen zwischen Räumen
def move(direction):
    global current_room
    if direction == "Norden" and current_room == "Start":
        current_room = "Raum1"
        print("Du gehst nach Norden.")
    elif direction == "Süden" and current_room == "Raum1":
        current_room = "Start"
        print("Du gehst nach Süden.")
    elif direction == "Osten" and current_room == "Raum1" and solved:
        current_room = "Schatzkammer"
        print("Du gehst nach Osten und betrittst die Schatzkammer!")
    else:
        print("Du kannst in diese Richtung nicht gehen.")

# Funktion zum Aufheben von Gegenständen
def take(item):
    global inventory
    if item in rooms[current_room]:
        inventory.append(item)
        rooms[current_room].remove(item)
        print(f"Du hast {item} aufgehoben.")
    else:
        print(f"Hier gibt es kein {item}.")


# Spielschleife
while True:
    command = input("Was möchtest du tun?('gehe Norden', 'nimm Buch', 'loese Raetsel'): ").lower()
    words = command.split()
    

    if words[0] == "gehe":
        move(words[1])
    elif words[0] == "nimm":
        take(words[1])
    elif words[0] == "loese" and words[1] == "raetsel":
        answer = input(riddle + " ")
        solve_riddle(answer)
    elif command == "beende":
        break
    else:
        print("Befehl nicht erkannt.")

    look_around()

    if current_room == "Schatzkammer":
        print("Herzlichen Glückwunsch! Du hast den Schatz gefunden!")
        break

