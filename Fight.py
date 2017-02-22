import random, ast


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
        player["HP"] -= enemy["Dmg"]
        enemy["HP"] -= player["Dmg"]
        print("What will you do? (Attack | Defend| Fall Back | Flee)")
        combat_choice = input()
        if combat_choice == "Attack":
            choose_fight_style(player["Prof"])
        elif combat_choice == "Defend":
            defend()
        elif combat_choice == "Fall Back":
            fall_back()
        elif combat_choice == "Flee":
            flee()
        else:
            print("invalid choice")
    if player["HP"] <= 0:
        print("You lose!")
    elif enemy["HP"] <= 0:
        print("You win!")


def choose_fight_style(player_prof):
    switcher = {
        "Archer": archer_fight,
        "Rogue": rogue_fight,
        "Warrior": warrior_fight,
    }
    fight_style = switcher.get(player_prof)
    return fight_style()


def archer_fight():
    print('pew pew')



def rogue_fight():
    print('stab stab')


def warrior_fight():
    print('slash slash')


def defend():
    print("Come back to this")


def fall_back():
    print("Come back to this")

def flee():
    print("Come back to this")