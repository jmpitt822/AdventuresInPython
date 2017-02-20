import ast
from ProfChoices import choose_prof

def greeting():
    player_name = input("Greetings, traveller. What is your name?\n")
    savedata["Name"] = player_name
    choose_prof(savedata)


f = open('savefile', 'r+')
read_file = f.read()
savedata = ast.literal_eval(read_file)
print(savedata)
greeting()
print(savedata)
sds = str(savedata)
f.write(sds)
