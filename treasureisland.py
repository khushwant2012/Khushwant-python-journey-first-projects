print('welcome to treasure island')
print(
    '''888                                                         d8b        888 
888                                                         Y8P        888 
888                                                                    888 
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b. 888.d8888b 888 
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b88888K     888 
888   888    88888888.d888888"Y8888b.888  888888    88888888888"Y8888b.888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.    888     X88888 
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 888 888 88P'888''' 
)
direction = input('which direction do you want to go? left or right? ')
if direction == 'left':
    action=input('do you want to swim or wait? ')
    if action == 'wait':
        door=input('which door you want to open? red, yellow or blue? ')
        if door == 'yellow':
            print('you win!')
        elif door == 'red':
            print('burned by fire. game over')
        elif door == 'blue':
            print('eaten by beasts. game over')
        else:
            print('you have chosen a door that does not exist. game over')
    elif action == 'swim':
        print('attacked by trout. game over')
    else:
        print('you have chosen an action that does not exist. game over')
else:
    print('game over')

        