import random, ast


def choose_enemy():
    array = []
    with open('enemies', 'r') as f:
        for line in f:
            array.append(line.strip())
    x = random.randrange(1, 3)
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
    if player["HP"] <= 0:
        print("You lose!")
    elif enemy["HP"] <= 0:
        print("You win!")