from sys import argv

script, user_name = argv

prompt = '>>> '

print "Hi, %s, I'm the %s script" %(user_name, script)
print "I'd like to ask you some questions"
print "Do you like me %s?" %(user_name)
likes = raw_input(prompt)

print "Where do you live, %s?" %(user_name)
live = raw_input(prompt)

print "What kind of computer do you use, %s" %(user_name)
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice""" %(likes, live, computer)
