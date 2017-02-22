import random, ast, Loot


def choose_enemy():
    array = []
    with open('enemies', 'r') as f:
        for line in f:
            array.append(line.strip())
    x = random.randrange(0, 8)
    random_enemy = array[x]
    f.close()
    enemy = ast.literal_eval(random_enemy)
    return enemy


def begin_fight(player, enemy):
    print("Watch out,", player["Name"], ",", enemy["Name"], "the", enemy["Prof"], "approaches!")
    while player["HP"] > 0 and enemy["HP"] > 0:
        print("Your health:", player["HP"])
        print("Enemy health:", enemy["HP"])
        print("What will you do? (Attack | Defend| Fall Back | Flee)")
        combat_choice = input()
        if combat_choice == "Attack":
            choose_fight_style(player["Prof"], player, enemy)
        elif combat_choice == "Defend":
            defend(player, enemy)
        elif combat_choice == "Fall Back":
            fall_back(player, enemy)
        elif combat_choice == "Flee":
            flee(player, enemy)
        else:
            print("invalid choice")
    if player["HP"] <= 0:
        print("You lose!")
    elif enemy["HP"] <= 0:
        print("You win!")
        Loot.generate_loot(player)


def choose_fight_style(player_prof, player, enemy):
    switcher = {
        "Archer": archer_fight,
        "Rogue": rogue_fight,
        "Warrior": warrior_fight,
    }
    fight_style = switcher.get(player_prof)
    return fight_style(player, enemy)


def archer_fight(player, enemy):
    player_dmg = random.randrange(0, player["Dmg"])
    enemy["HP"] -= player_dmg
    print(player["Name"], "hit for", player_dmg)
    if player["Range"] <= enemy["Speed"]:
        enemy_dmg = random.randrange(0, enemy["Dmg"])
        player["HP"] -= enemy_dmg
        print(enemy["Name"], "hit for", enemy_dmg)
    print("The enemy is still", player["Range"], "yards away.")


def rogue_fight(player, enemy):
    player_dmg = random.randrange(0, player["Dmg"])
    enemy["HP"] -= player_dmg
    enemy_sight = random.randrange(0, 20)
    print(player["Name"], "hit for", player_dmg)
    if player["Stealth"] > enemy_sight:
        player["Stealth"] -= 3
    else:
        player["Stealth"] = 0
        enemy_dmg = random.randrange(0, enemy["Dmg"])
        player["HP"] -= enemy_dmg
        print(player["Name"], "was spotted!")
        print(enemy["Name"], "hit for", enemy_dmg)


def warrior_fight(player, enemy):
    player_rage = 0
    if player["HP"] < 20:
        player_rage = random.randrange(1, player["Rage"])
        print(player["Name"],"is raging!", player_rage)
    player_dmg = random.randrange(0, player["Dmg"])
    enemy_dmg = random.randrange(0, enemy["Dmg"])
    print(player["Name"], "hit for", player_dmg + player_rage)
    print(enemy["Name"], "hit for", enemy_dmg)
    player["HP"] -= enemy_dmg
    enemy["HP"] -= (player_dmg + player_rage)


def defend(player, enemy):
    player_def = random.randrange(0, player["Def"])
    if player_def < enemy["Dmg"]:
        player["HP"] -= (enemy["Dmg"] - player_def)
    print(player["Name"], "defended for", player_def, "against", enemy["Dmg"], "damage.")


def fall_back(player, enemy):
    if player["Speed"] > enemy["Speed"]:
        player["Speed"] -= (enemy["Speed"]/2)
        if player["Prof"] == "Archer":
            player["Range"] += 5
    else:
        enemy_dmg = int((enemy["Dmg"] * 0.75))
        player["HP"] -= enemy_dmg
        print(player["Name"], "was too slow! They took", enemy_dmg, "damage.")


def flee(player, enemy):
    if player["Speed"] > enemy["Speed"]:
        print("You got away safely!")
        exit()
    else:
        print(player["Name"], "couldn't get away! They took", enemy["Dmg"], "damage.")
        player["HP"] -= enemy["Dmg"]