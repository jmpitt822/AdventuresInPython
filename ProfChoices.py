
def choose_prof(savedata):
    print("Hello,", savedata["Name"], ", what is your profession?(Archer | Rogue | Warrior)")
    player_prof = input()
    if player_prof == "Archer":
        savedata["Prof"] = player_prof
        choose_archer_weap(savedata)
    elif player_prof == "Rogue":
        savedata["Prof"] = player_prof
        choose_rogue_weap(savedata)
    elif player_prof == "Warrior":
        savedata["Prof"] = player_prof
        choose_warrior_weap(savedata)
    else:
        print("Choose again, traveller.")

def choose_archer_weap(savedata):
    print("Ah, an archer, eh? What bow do you favor? (Crossbow | Longbow | Recurve)")
    player_weap = input()
    if player_weap == "Crossbow":
        print("Slow, but sturdy enough.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 8
        savedata["HP"] = 25
    elif player_weap == "Longbow":
        print("Can't beat the classics.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 5
        savedata["HP"] = 20
    elif player_weap == "Recurve":
        print("You prefer the fancy stuff, eh?")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 10
        savedata["HP"] = 15
    else:
        print("Choose again")

def choose_rogue_weap(savedata):
    print("Sneak and stab, right? Or do you prefer to shoot? (Daggers | Shortbow | Pistol)")
    player_weap = input()
    if player_weap == "Daggers":
        print("Nothing's as silent as a blade.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 10
        savedata["HP"] = 25
    elif player_weap == "Shortbow":
        print("They'll never hear it coming.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 5
        savedata["HP"] = 20
    elif player_weap == "Pistol":
        print("Not the most stealthy weapon, is it?")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 10
        savedata["HP"] = 15
    else:
        print("Choose again.")

def choose_warrior_weap(savedata):
    print("Hail, warrior! How do you smite your foes? (Sword & Shield | Longsword | Axe)")
    player_weap = input()
    if player_weap == "Sword & Shield":
        print("You have to be able to give as good as you get.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 10
        savedata["HP"] = 40
    elif player_weap == "Longsword":
        print("The best defense is a good offense.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 20
        savedata["HP"] = 25
    elif player_weap == "Axe":
        print("Brutal, but effective.")
        savedata["Weapon"] = player_weap
        savedata["Dmg"] = 25
        savedata["HP"] = 15
    else:
        print("Choose again.")