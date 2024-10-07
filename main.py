from game_utils import solve_riddle, end_game

def greeting():
    print("Willkommen im Abenteuer-Spiel!")
    print("Du wirst durch verschiedene Räume navigieren und Rätsel lösen müssen, um den Schatz zu finden.")
    print("Gib 'norden', 'süden', 'osten' oder 'westen' ein, um dich zu bewegen.")

def enter_room(room):
    descriptions = {
        "start": "Du bist in einem dunklen Raum. Es gibt Türen nach Norden und Osten.",
        "room_north": "Du bist in einem Raum mit alten Büchern. Es gibt Türen nach Süden und Osten.",
        "room_east": "Du bist in einem geheimen Raum voller Goldmünzen. Der Schatz ist hier!",
    }
    print(descriptions[room])
    
    actions = {
        "start": ["norden", "osten"],
        "room_north": ["süden", "osten"],
        "room_east": []
    }
    
    return actions[room]

def game_loop():
    current_room = "start"
    while True:
        actions = enter_room(current_room)
        if current_room == "room_east":
            print("Herzlichen Glückwunsch! Du hast den Schatz gefunden!")
            end_game()
            break
        
        command = input("Was möchtest du tun? ").strip().lower()
        
        if command in actions:
            if command == "norden":
                current_room = "room_north"
                riddle = "Ich bin nicht lebendig, aber ich wachse. Ich habe keine Lungen, aber ich brauche Luft. Was bin ich?"
                if solve_riddle(riddle):
                    print("Rätsel gelöst! Du darfst weitergehen.")
            elif command == "osten":
                if current_room == "start":
                    current_room = "room_east"
                else:
                    print("Du kannst nicht nach Osten gehen.")
            elif command == "süden":
                if current_room == "room_north":
                    current_room = "start"
                else:
                    print("Du kannst nicht nach Süden gehen.")
            else:
                print("Ungültiger Befehl.")
        else:
            print("Du kannst in diese Richtung nicht gehen.")

if __name__ == "__main__":
    greeting()
    game_loop()