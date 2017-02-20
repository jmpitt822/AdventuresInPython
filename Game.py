savedata = {}


def greeting():
    player_name = input("Greetings, traveller. What is your name?\n")
    savedata["Name"] = player_name
    choose_prof()


def choose_prof():
    print("Hello,", savedata["Name"], ", what is your profession?(Archer | Rogue | Warrior)")
    player_prof = input()
    if player_prof == "Archer":
        savedata["Prof"] = player_prof
        # choose_archer_weap()
    elif player_prof == "Rogue":
        savedata["Prof"] = player_prof
        # choose_rogue_weap()
    elif player_prof == "Warrior":
        savedata["Prof"] = player_prof
        # choose_warrior_weap()
    else:
        print("Choose again, traveller.")


# def choose_archer_weap():
#     print("Ah, an archer, eh? What bow do you favor? (Crossbow | Longbow | Recurve Bow)\n")
#     while savedata



greeting()
