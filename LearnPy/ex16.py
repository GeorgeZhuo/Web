from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN"

raw_input("?")

print "Open the file.."
target = open(filename, 'w')

print "Truncateing the file. Goodbye"
target.truncate()

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

target.close()
print "We test the write() function: "

target = open(filename)
print target.read()


