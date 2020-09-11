from time import sleep
import sys

CHAR_DELAY = 0.02
NEWLINE_DELAY = 0.25

def stateful(room_func, initial_state={}):
    state_obj = initial_state
    def wrapped_func():
        nonlocal state_obj
        return room_func(state_obj)
    return wrapped_func

def spooky_print(text):
    c_delay = CHAR_DELAY
    l_delay = NEWLINE_DELAY
    
    lines = text.split("\n")
    
    if len(lines) > 10:
        c_delay *= 0.1
        l_delay *= 5/len(lines)
        
    
    for line in text.split("\n"):
        print("🍆 ", end='')
        if c_delay == 0:
            print(line, end='')
        else:
            for c in line:
                print(c, end='')
                sys.stdout.flush()
                sleep(c_delay)
        
        print()
        sleep(l_delay)
    print()

def get_player_name():
    spooky_print("Yo -- what's your name?")
    return input("> ") or "Kara Anderson"



def get_user_action(valid_actions=list(interactions.keys())):
    cmd = input("🍑 ").lower()
    
    for verb in valid_actions:
        if cmd.startswith(verb):
            return verb, cmd[len(verb):].strip()
        
    return cmd, None

def do_action():
    action, obj = get_user_action()
    if obj in interactions[verb]:
        spooky_print(f"""You {verb} {article} {obj}""")

@stateful(initial_state={
    'fireplace_lit': False
})
def entryway(state_obj):
    spooky_print("""
        The front door creeks open, you enter a hallway. The carpet is thick with dust. 
        You hold up your lighter to find a light switch none are near you.
        But there is a candelabra on the entryway table.""")
    
    interactions = {
        "light": 'fireplace',
        "look": None,
        "grab": None,
        "pick up": None,
    }
    
    do_action(interactions)
    

def play():
    spooky_print(f"""Dear {PLAYER['name']},
        I have lived a life of many adventures, through them I have acquired a substantial collection of rare artifacts 
        that have both archaeological and historical importance. One might call it treasure. 
        I have left in a secure location, go the the Chateau and find it. Only a worthy heir can recover it.
        
        Love, 
        your estranged grandfather
        Percival Montclaire
        
        --------------------------------
        
        You read the letter over again as the taxi pulls up to the house.  What does it mean? 
        Why are you here?  What is the treasure?  Who is Percival!?
        
        You exit the taxi and look at the creepy house.
        
        You pull open the door and step inside.  The door slams shut behind you.""")
    entryway()



if __name__ == '__main__':
    PLAYER = {
        'name': get_player_name(),
        'inventory': []
    }
    
    play()