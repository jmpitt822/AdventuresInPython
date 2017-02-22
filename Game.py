import ast
from ProfChoices import choose_prof
from Fight import choose_enemy, begin_fight


def greeting():
    player_name = input("Greetings, traveller. What is your name?\n")
    savedata["Name"] = player_name
    choose_prof(savedata)

savedata = {}
player_loot = []
print("What would you like to do? \n>> 1. New Game\n>> 2. Load Game")
menu_choice = input()
if menu_choice == "1" or menu_choice == "New Game":
    greeting()
    sds = str(savedata)
    nf = open('savefile_'+savedata["Name"]+'.txt', 'w')
    nf.write(sds)
    starting_loot = {'Name': 'Health Potion', 'Value': 10}
    ssl = str(starting_loot)
    nf.write('\n'+ssl)
    nf.close()
elif menu_choice == "2" or menu_choice == "Load Game":
    load_choice = input("Which character do you want to load?\n")
    f = open('savefile_'+load_choice+'.txt', 'r')
    read_file = f.read()
    f.close()
    data_list = read_file.split('\n')
    savedata = ast.literal_eval(data_list[0])
    for x in data_list:
        if "Value" in x:
            dict_x = ast.literal_eval(x)
            player_loot.append(dict_x)
    print(savedata)
    print(player_loot)
else:
    print("Invalid choice")
enemy = choose_enemy()
begin_fight(savedata, enemy)
