class Other(object):

    def override(self):
        print ("Other override()")
    
    def implicit(self):
        print ("Other implicit()")

    def altered(self):
        print ("Other altered()")

def Child(object):

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.imlicit()

    def override(self):
        print ("Child override()")

    def altered(self):
        print ("Child, Before Other altered()")
        self.other.altered()
        print ("Child, After Other altered")

son = Child()

son.implicit()
son.override()
son.altered()