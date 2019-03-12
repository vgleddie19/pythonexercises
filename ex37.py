ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "Where adding into your stuff: %s" % next_one
    print "There's %d item now." % len(stuff)

print "There we go:", stuff
print "Let's do some things with the stuff."

print "execute this stuff[1]: "
print "%s\n" % stuff[1]

print "execute this stuff[0]: "
print "%s\n" %  stuff[0]

print "execute this stuff[-1]: "
print "%s\n" %  stuff[-1]

print "execute this stuff.pop(): "
print "%s\n" %  stuff.pop()

print "execute this ' '.join(stuff): "
print "%s\n" %  ' '.join(stuff)

print "execute this '#'.join(stuff[3:5]): "
print "%s\n" %  '#'.join(stuff[3:5])