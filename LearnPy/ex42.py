# this the code of class

class TheThing:
    number = 0
    def __int__(self):
        self.number = 0

    def some_function(self):
        print "Now, I am called"

    def add_number(self, more):
        self.number += more
        return self.number

# two defferent things

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_number(20)
print a.add_number(20)
print b.add_number(30)
print b.add_number(30)

print a.number
print b.number
