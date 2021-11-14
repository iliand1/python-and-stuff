<<<<<<< HEAD
import time
"""
Simple console choice driven horror game with simple story.
"""


def part_1():
    """This is the first part of the text game"""
    print("Hello, you're playing my game right now, so enjoy!!")
    time.sleep(2)
    print("""
    You're a group of friends: Joyce, Tom, Elijah and you, the player.
    You decided to go on a camp trip in the woods near a sketchy place that is 
    known to be a place of satanists.
    Drunk and feeling young, you put your tents up, but before you know it, 
    it will be the last night for some of you.""")
    time.sleep(2)
    print("""
    While having a good time drowning yourself in alcohol, you seem 
    to feel an evil presence quietly watching over you.
    After a while, Tom wants to have a piss, thus wandering into the darkness to find some privacy.
    Having left, you don't notice how a few hours have passed, and Tom doesn't feel like coming back.
    Unlike Joyce and Elijah, who are having the best time of their life, you feel an increasing anxiety
    growing inside your chest, so you feel obliged to look for your comrade.

    """)
    time.sleep(2)
    a = input("Are you ready to go?\nYour answer: ").lower()
    time.sleep(2)
    if a=="yes":
        print("""
    "I'll go find that dumbass, so wait for a while". You go into the darkness, bringing your trusty flashlight.
    You try desperately to find your friend, but with no luck. Suddenly, you hear a faint scream in the
    direction of your camp. Running back to the camp, you find it wrecked, with no one to be seen. 
    But wait... there's a faint trail of blood on the ground, maybe it could help you in some way?
        """)
        time.sleep(2)
        a = input("Follow it?\nYour answer: ").lower()
        if a=="yes":
            print("""
    You hesitantly follow the crimson trail, hoping it would lead somewhere more comforting than a half-wrecked 
    camp and certainly not adark and unfriendly wild nature. You follow the trail. One hour passes... Two hours...
    And then, you notice a small lightsource in the distance!"Safety!", you think. You quietly approach the source,
    which appears to be the front yard of a lonely cabin. You shyly knock on the door, but to no answer.
    Hearing a load spooky noise in the vicinity, you decide to rather face the angry owner of the cabin than deal with 
    that "something". So you quickly open the door,which to your surprise wasn't locked(although, why look your door 
    in a place where you're basically alone?), and get inside.
            """)
            time.sleep(4)
            print("END OF PART I.")
            time.sleep(40)
        else:
            print("""
    You decide: fuck that! I'd rather re-do my tent and wait for everybody, I'm sure those drunk fucks pulled a prank on me...
    Having put up your tent once again, you try to get some sleep, but just can't. You really feel being observed. With a sigh,
    you put yourself out of your misery by drinking what was left of the booze, and feeling nothing, you plunge into a tipsy 
    sleep.You've woken up to the sound of some chant. You try to budge, but fail, noticing being hung by chains by every limb
    of your body.And you notice that you have a pentagram cut out on your torso, the wound being cauterized. How nice of them!
    But their hospitality stops here.Now they begin torturing you, and needless to say that you've quickly died of shock. 
    Who would've guessed that having your guts taken out of you is so unpleasant :-)
            """)
            time.sleep(1)
            print("You died a most gruesome death!")
            time.sleep(40)
    else:
        print("""
    "I'm sure he's fine, they say beasts are more scared of humans than vice-versa". You continue
    sitting by the campfire with your friends, when a dark figure appears on the edge of the light
    emitted by the fire. You feel relieved that you haven't lost your friend, but something feels off... 
    That "thing" is holding an axe in its hand! You pay no notice at first, but then Joyce starts screaming,
    as the humanoid creature swung the axe in close proximity to her face. You all freak out, and before you know it,
    you have all run in different directions,all alone in the dark... Until you find that creature! Drenched in blood,
    it screams and leaps towards you, effectively ending your life.
        """)
        time.sleep(1)
        print("You died! It's that simple.")
        time.sleep(40)


if __name__=="__main__":
=======
import time
"""
Simple console choice driven horror game with simple story.
"""


def part_1():
    """This is the first part of the text game"""
    print("Hello, you're playing my game right now, so enjoy!!")
    time.sleep(2)
    print("""
    You're a group of friends: Joyce, Tom, Elijah and you, the player.
    You decided to go on a camp trip in the woods near a sketchy place that is 
    known to be a place of satanists.
    Drunk and feeling young, you put your tents up, but before you know it, 
    it will be the last night for some of you.""")
    time.sleep(2)
    print("""
    While having a good time drowning yourself in alcohol, you seem 
    to feel an evil presence quietly watching over you.
    After a while, Tom wants to have a piss, thus wandering into the darkness to find some privacy.
    Having left, you don't notice how a few hours have passed, and Tom doesn't feel like coming back.
    Unlike Joyce and Elijah, who are having the best time of their life, you feel an increasing anxiety
    growing inside your chest, so you feel obliged to look for your comrade.

    """)
    time.sleep(2)
    a = input("Are you ready to go?\nYour answer: ").lower()
    time.sleep(2)
    if a=="yes":
        print("""
    "I'll go find that dumbass, so wait for a while". You go into the darkness, bringing your trusty flashlight.
    You try desperately to find your friend, but with no luck. Suddenly, you hear a faint scream in the
    direction of your camp. Running back to the camp, you find it wrecked, with no one to be seen. 
    But wait... there's a faint trail of blood on the ground, maybe it could help you in some way?
        """)
        time.sleep(2)
        a = input("Follow it?\nYour answer: ").lower()
        if a=="yes":
            print("""
    You hesitantly follow the crimson trail, hoping it would lead somewhere more comforting than a half-wrecked 
    camp and certainly not adark and unfriendly wild nature. You follow the trail. One hour passes... Two hours...
    And then, you notice a small lightsource in the distance!"Safety!", you think. You quietly approach the source,
    which appears to be the front yard of a lonely cabin. You shyly knock on the door, but to no answer.
    Hearing a load spooky noise in the vicinity, you decide to rather face the angry owner of the cabin than deal with 
    that "something". So you quickly open the door,which to your surprise wasn't locked(although, why look your door 
    in a place where you're basically alone?), and get inside.
            """)
            time.sleep(4)
            print("END OF PART I.")
            time.sleep(40)
        else:
            print("""
    You decide: fuck that! I'd rather re-do my tent and wait for everybody, I'm sure those drunk fucks pulled a prank on me...
    Having put up your tent once again, you try to get some sleep, but just can't. You really feel being observed. With a sigh,
    you put yourself out of your misery by drinking what was left of the booze, and feeling nothing, you plunge into a tipsy 
    sleep.You've woken up to the sound of some chant. You try to budge, but fail, noticing being hung by chains by every limb
    of your body.And you notice that you have a pentagram cut out on your torso, the wound being cauterized. How nice of them!
    But their hospitality stops here.Now they begin torturing you, and needless to say that you've quickly died of shock. 
    Who would've guessed that having your guts taken out of you is so unpleasant :-)
            """)
            time.sleep(1)
            print("You died a most gruesome death!")
            time.sleep(40)
    else:
        print("""
    "I'm sure he's fine, they say beasts are more scared of humans than vice-versa". You continue
    sitting by the campfire with your friends, when a dark figure appears on the edge of the light
    emitted by the fire. You feel relieved that you haven't lost your friend, but something feels off... 
    That "thing" is holding an axe in its hand! You pay no notice at first, but then Joyce starts screaming,
    as the humanoid creature swung the axe in close proximity to her face. You all freak out, and before you know it,
    you have all run in different directions,all alone in the dark... Until you find that creature! Drenched in blood,
    it screams and leaps towards you, effectively ending your life.
        """)
        time.sleep(1)
        print("You died! It's that simple.")
        time.sleep(40)


if __name__=="__main__":
>>>>>>> 68a8548c94e7fe1d4d679d0f40254b37b556010b
    part_1()