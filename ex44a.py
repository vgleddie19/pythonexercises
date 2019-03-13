class Parent(object):
    def implicit(self):
        print "PARNET implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()