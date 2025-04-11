# Adrian Estrada
rooms = {
    'Mount Olympus': {'South': 'Ares Peak', 'East': 'Athena\'s Room', 'Item': ''},
    'Ares Peak': {'South': 'Poseidon\'s Lake', 'East': 'Hera\'s Room', 'West': 'Hestia\'s Room', 'North': 'Mount Olympus','Item': 'Ares Blessing'},
    'Poseidon\'s Lake': {'South': 'Hades Portal', 'East': 'Apollo\'s View', 'North': 'Ares Peak', 'Item': 'Trident'},
    'Hades Portal': {'North': 'Poseidon\'s Lake', 'Item': 'Hades Army'},
    'Apollo\'s View': {'West': 'Poseidon\'s Lake', 'Item': 'Apollos Bow'},
    'Hera\'s Room': {'West': 'Ares Peak', 'Item': 'Scepter', },
    'Hestia\'s Room': {'East': 'Ares Peak', 'Item': 'Sacred Flame'},
    'Athena\'s Room': {'West': 'Mount Olympus', 'North': 'Throne Room', 'Item': 'Shield'},
    'Throne Room': {'Item': 'Zeus'},
}
state = 'Mount Olympus'


def get_new_state(state, direction):
    new_state = state
    if direction.capitalize() in rooms[state]: # searches rooms if direction exist in specific room
        new_state = rooms[state][direction.capitalize()] # updates new_state
    return new_state


def get_item(state):
    return rooms[state]['Item'] # searches for item in rooms using state as a key


def show_instructions():
    # prints out basic instructions for the user
    print('Find 7 items to defeat zeus.')
    print('Move commands: South, North, East, West')
    print("Add to Inventory: get 'item_name'")

def show_direction(state):
    compass_list = rooms.get(state, {}) #gets a list of rooms using room keys

    print("You can go:")

    for compass in ['North', 'South', 'East', 'West']: #searches for directions in rooms
        if compass in compass_list:
            print(f"{compass} -> {compass_list[compass]}") #list out path and room available
        else:
            print(f"{compass} -> No Available direction") # if a direction does not exist prints this out


def show_menu():
    global item # global so then main can access it

    #prints out basic menu
    print('--------------------')
    print('You are in ', state)
    show_direction(state)
    print()
    print('Inventory:', Inventory)
    item = get_item(state)
    print('You see a', item)
    print('--------------------')




show_instructions()
Inventory = []
#items = ['Ares Blessing','Trident','Hades Army', 'Apollos View', 'Scepter', 'Scared Flame', 'Shield']

while (1):

    show_menu() #takes you to def Show_menu


    if item == 'Zeus': #end the game if player ends up in Throne room before collecting all items
        print('Zeus flung a bolt of lightning')
        exit(0)

    direction = input('Enter your move: ').strip().lower()

    if direction in ['north', 'south', 'east', 'west']:
        new_state = get_new_state(state, direction) #takes values state and direction into def function

        if new_state == state:
            print('There is not path there')
        else:
            state = new_state # updates state

    elif direction.startswith('get '): # if player types get to pick up item runs this statement
        entered_item = direction[4:].strip() # gets rid of get and leading space

        if entered_item.lower() == item.lower(): # compares user input with item in current room
            if item in Inventory:
                print('You are carrying this') # if the user has the item runs this
            else:
                Inventory.append(item) #adds item to Inventory


    else:
        print('Invalid input or move or item')

    if len(Inventory) == 7: #once the user collects all items game ends
        print('Zeus I will defeat you right here')
        print('I will show you the might of the gods')
        print('You defeated Zeus and became the new ruler of the Gods')
        exit(0)