class Parent(object):

    def override(self):
        print ("PARENT override()")
    def implicit(self):
        print ("PARENT implicit()")

    def altered(self):
        print ("PARENT altered()")

class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, Before Parent altered()")
        print(Child,self).altered()
        print("Child, After Parent altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
dad.altered()