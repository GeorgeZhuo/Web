print "Let;s practice everything"
print "You\'d need to know \' bout escapt  with \\ that \n newlines an \t tabs"

poem = """
\t The ovely world with logic so firmly planted
cannot dicern \n the needs of love 
and requires an explantion.
\n\t\twhere there is none.
"""

print "---------------------" 
print poem
print "---------------------"

five = 10 - 2 + 3 - 6

print "This should be five: %d" %five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 10000
    crates = jars / 100
    return jelly_beans, jars, crates

started = 10000
jelly, jars, crates = secret_formula(started)

print "jelly: %d, jars: %d, crates: %d" %(jelly, jars, crates)
print "jelly: %d, jars: %d, crates: %d" %secret_formula(started)
