import random, ast

def generate_loot(player):
    array = []
    with open('loot_table', 'r') as f:
        for line in f:
            array.append(line.strip())
    x = random.randrange(0, 4)
    random_loot = array[x]
    f.close()
    savefile = open('savefile_'+player["Name"]+'.txt', 'a+')
    savefile.write('\n'+random_loot)
    savefile.close()
    loot = ast.literal_eval(random_loot)
    print(player["Name"], "found a ", loot["Name"],".")
