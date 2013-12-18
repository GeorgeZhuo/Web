# this is the 18 execise about function

def print_two(*args):
    arg1, arg2 = args
    print "args: %r, %r\n" %(arg1, arg2)

def print_one(arg):
    print "arg: %r\n" %arg

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r\n" %(arg1, arg2)

def print_none():
    print "This is about nothing\n"

print_two("George", "Sansan")
print_one("George")
print_two_again("George", "Sansan")
print_none()
