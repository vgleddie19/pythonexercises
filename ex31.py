print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

print "Input 1 or 2: \n"
door = raw_input("======> ")

if(door == "1"):
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the Cake."
    print "2. Scream at the bear"
    print "Input 1 or 2: \n"
    bear = raw_input("======> ")

    if bear == "1":
        print "The bear eats your face off. You died!"
    elif bear == "2":
        print "The bear eats your legs off. Goodbye!"
    else:
        print "Well, doing %s is probably better. bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss and Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Undestanding revolvers yelling melodies"

    print "Input 1, 2, or 3: \n"
    insanity = raw_input("======> ")
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello, Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Goodbye!"
else:
    print "You stumble around and fall on a knife and die. Goodbye!"