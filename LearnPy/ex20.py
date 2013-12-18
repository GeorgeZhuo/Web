# function and file

from sys import argv

script, input_file = argv

def read_file(current_file):
    print current_file.read()

def rewind(current_file):
    current_file.seek(0)

def read_line(current_line, current_file):
    print current_line, current_file.readline()

filename = open(input_file)

print "Print the all file"
read_file(filename)

print "Now, Let's rewind the file, like tape"
rewind(filename)

line_count = 1
read_line(line_count, filename)

line_count += 1
read_line(line_count, filename)

line_count += 1
read_line(line_count, filename)
