"""A game for encouragement and/or minor procrastinators. I attempted a game loop--see maybe_end below. :)
Not sure if I met the other above-and-beyond portion..."""

from random import randint

__author__ = "730429981"

SILLY_FACE: str = "\U0001F92A"
CUTIE_PIE: str = "\U0001F970"
BIG_HUGS: str = "\U0001F917"
WATER_POWER: str = "\U0001F30A"
STAR_STRUCK: str = "\U0001F929"
BIG_LOVE: str = "\U0001F496"
STRONGER_THAN_YOU_THINK: str = "\U0001F4AA"
BEE_POSITIVE: str = "\U0001F41D"
FIRE_POWER: str = "\U0001F525"
YOU_ARE_MY_SUNSHINE: str = "\U00002600"
WISE_BIRDIE: str = "\U0001F989"
WALKIE_TALKIE: str = "\U0001F99C"
CHILLY_BIRDIE: str = "\U0001F427"
RUBBER_DUCKY: str = "\U0001F986"
MANGO_TANGO: str = "\U0001F96D"
COCO_LOCO: str = "\U0001F965"
SPINY_SWEET: str = "\U0001F34D"
BANANANANA: str = "\U0001F34C"
SUNFLOWER_POWER: str = "\U0001F33B"
TWO_LIP: str = "\U0001F337"
VERY_CHERRY: str = "\U0001F338"
HI_BI: str = "\U0001F33A"
BUILD_ME_UP: str = "\U0001F33C"
TINTED_GLASSES: str = "\U0001F339"

player: str
points: int

def greet() -> None: 
    """Weclome message"""
    global player
    player = input("Welcome to my lil quiz! What should I call ya? ")

def maybe_end() -> None:
    """implementation of game loop, allowing player to end or continue the game 
    after completing a branch of gameplay"""
    print(f"You've got {points} points!")
    while input(f"Play again? {STAR_STRUCK}--yeah/nah: ") == "yeah":
        print(f"Okay, let's go again and rack up some more points!")
        get_started()
    not_today()

def not_today() -> None:
    """For the ones who just aren't in the mood; also destination for players who choose not to replay"""
    while input(f"Are you sure you want to go, {player}? {BIG_LOVE} yes/no-- ") == "no":
        print(f"Awesome! Let's play again {CUTIE_PIE}")
        get_started()
    print(f"I'll let ya go, {player}; you finished with {points} points. Have a lovely day! {BIG_HUGS}")
    quit()

def feel_better(points: int) -> int:
    """For the ones feeling a lil down"""
    while input(f"Need more positivity, {player}? yes/no: ") == "yes":
        print(f"I gotchu, {player} {BIG_HUGS}")
        points += 1
        choose_chill: str = str(input(f"Let's turn that frown upside-down, {player}! -choose- or -chill-? "))
        points += 1
        if choose_chill == "choose":
            ha_ha: str = str(input(f"Sure, {player}! Want a -quote- or -joke-? "))
            points += 1
            if ha_ha == "quote":
                y: int = randint(1, 3)
                if y <= 2:
                    if y == 2:
                        print("'The darkest hour of the night comes just before the dawn.' (Thomas Fuller)")
                        print(f"{YOU_ARE_MY_SUNSHINE}{YOU_ARE_MY_SUNSHINE}{YOU_ARE_MY_SUNSHINE}")
                        points += 1
                    else:
                        print("'Feel the fact that you are enough.' (Mark Nepo)")
                        print(f"{BIG_LOVE}{BIG_HUGS}{BIG_LOVE}")
                else:
                    print("'You can't stop the waves, but you can learn to swim.' (Jon Zinn)")
                    print(f"{WATER_POWER}{WATER_POWER}{WATER_POWER}")
            if ha_ha == "joke":
                z: int = randint(1, 3)
                if z <= 2:
                    if z == 1:
                        print("What do you call a nosy pepper?")
                        print(f"Jalapeño business! {SILLY_FACE}")
                    else:
                        print("How much does a pirate pay for corn?")
                        print(f"A buccaneer! {SILLY_FACE}")
                else:
                    print("Does an apple a day keep the doctor away?")
                    print(f"Only if you throw it hard enough! {SILLY_FACE}")
        if choose_chill == "chill":
            print(f"Don't worry, I'll do the work--just breathe {BIG_LOVE}")
            x: int = randint(1, 4)
            if x <= 3: 
                if x == 2 or x == 3:
                    print(f"it's okay to not be okay right now, {player} {BIG_HUGS}")
                    points += 1
                else: 
                    print(f"tomorrow is a new day, {player}--hang in there! {STRONGER_THAN_YOU_THINK}")
                    points += 1
            else:
                print(f"keep bee-ing positive, {player} {BEE_POSITIVE}")
                points += 1
    print(f"Hope things are looking up, {player} {BIG_LOVE}")
    return points

def get_started() -> None:
    """The starting point of the game, where user input -meh- allows user to end the game;
    also return point for replay"""
    first_q: str = str(input(f"How are ya feeling? Type -solid- or -rough- to play. Type -meh- to end: "))
    global points
    if first_q == "solid" or "rough" or "meh":
        if first_q == "solid":
            points += 1
            good_feels(first_q)
        if first_q == "rough":
            points = feel_better(points)
            # Have passed in player's points as arg in call
            # And updated the global points var using the local points in feel_better
            maybe_end()
        if first_q == "meh":
            points += 1
            not_today()

def good_feels(choices: str) -> None:
    """For the ones who are feelin' good"""
    choice_one: int = int(input(f"To get started, pick a number between 1 and 4: "))
    global points
    points += 1        
    if choice_one <= 3:
        if choice_one == 1:
            print(f"Let's find out which powerful thing you're most like, {player}.")
            choice_a: str = str(input(f"Gimme a colour! Pick between blue/red/yellow: "))
            points += 1
            if choice_a == "blue":
                print(f"You seem pretty zen, {player}.")
                print(f"But like the ocean, there's power under that calm surface {WATER_POWER}")
                maybe_end()
            if choice_a == "red":
                print(f"{player}, your spark ignites others' energy--just like fire {FIRE_POWER}")
                maybe_end()
            else:
                print(f"You've a sunshiny warmth that draws others to you, {player} {YOU_ARE_MY_SUNSHINE}")
                maybe_end()
        if choice_one == 2:
            print(f"What bird are you? Let's find out, {player}!")
            choice_b: str = str(input("How would you describe yourself? chill/energetic: "))
            points += 1
            if choice_b == "chill":
                choice_c: str = str(input(f"Love it, {player}! What do you prefer--cook/takeout: "))
                points += 1
                if choice_c == "cook":
                    print(f"You're an {WISE_BIRDIE}! Your quiet strength + independence is cool, {player}.")
                    maybe_end()
                else:
                    print(f"We've got a {CHILLY_BIRDIE}! Love your go-with-the-flow mentality, {player}.")
                    maybe_end()
            else: 
                choice_d: str = str(input("Which friends do you like to hang out with most? new/old: "))
                points += 1
                if choice_d == "new":
                    print(f"{player}, you're almost certainly a {WALKIE_TALKIE}--super fun + spontaneous.")
                    maybe_end()
                else: 
                    print(f"We've got a {RUBBER_DUCKY} on our hands!")
                    print(f"Most don't notice how hard you work, but it'll pay off, {player}.")
                    maybe_end()
        if choice_one == 3:
            print(f"What fruit are you most like, {player}? Let's find out!")
            choice_e: str = str(input("Choose your favourite place to go to start--out/in: "))
            points += 1
            if choice_e == "out":
                choice_f: str = str(input("What do you like better? sweet/savoury: "))
                points += 1
                if choice_f == "sweet":
                    print(f"I think you're a {MANGO_TANGO}: kind, outgoing, and compassionate.")
                    maybe_end()
                else:
                    print(f"{COCO_LOCO}s represent! Your ability to adapt makes you an asset to any group.")
                    maybe_end()
            else:
                choice_g: str = str(input("Which films do you like better--action/comedy: "))
                points += 1
                if choice_g == "action":
                    print(f"Oooo, a {SPINY_SWEET} for sure! A spiky exterior protects your sweet spirit...")
                    print(f"but trust is good too, {player}.")
                    maybe_end()
                else:
                    print(f"You're a reliable go-to person, {player}--like a {BANANANANA}. Keep being you!")
                    maybe_end()                  
    else:
        print(f"Which flower are you, {player}? Let's get to it!")
        choice_h: str = str(input("Give me a letter--a/b/c: "))
        points += 1
        if choice_h == "a":
            choice_i: str = str(input("I need a little more info--what's superior, light or dark? "))
            points += 1
            if choice_i == "light":
                print(f"You've got a sunny disposition, {player}--just like a {SUNFLOWER_POWER}!")
                maybe_end()
            else: 
                print(f"Like a {TWO_LIP}, you've pushed through tough times to become this wonderful you.")
                maybe_end()
        if choice_h == "b":
            choice_j: str = str(input("I need a little more info--what's your favourite, winter or summer? "))
            points += 1
            if choice_j == "winter":
                print(f"You're a {VERY_CHERRY}--you give people hope when times are rough, {player}.")
                maybe_end()
            else:
                print(f"You just might be a {HI_BI}: you go big, and people love you for it.")
                maybe_end()
        if choice_h =="c": 
            choice_k: str = str(input("I need a little more info--choose one gold or silver: "))
            points += 1
            if choice_k == "gold": 
                print(f"Oh, a {BUILD_ME_UP}! You take joy in the little things, {player}--never stop.")
                maybe_end()
            else:
                print(f"As a {TINTED_GLASSES}, people find you mysterious...")
                print(f"your love of the darkly beautiful is unique.")
                maybe_end()

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    """For sake of clarity, play moves to get_started, which has the 3 play options."""
    greet()
    print(f"Okie dokie, { player }!")
    global points
    points = 0
    points += 1
    print(f"You've already got { points } points! Let's earn some more {CUTIE_PIE}{SILLY_FACE}")
    get_started()

if __name__ == "__main__":
    main()