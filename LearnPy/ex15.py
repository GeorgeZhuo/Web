from sys import argv

script, filename = argv

txt = open(filename)

print "Here is you file: %r" % filename
print txt.read()

print "I will also ask you to type it again:"
file_again = raw_input(">> ")
txt.close()

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
