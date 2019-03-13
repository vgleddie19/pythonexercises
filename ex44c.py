class Parent(object):
    def altered(self):
        print "Parent alter()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()        
        print "CHILD AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()