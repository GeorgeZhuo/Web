def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese" %cheese_count
    print "You have %d crackers" %boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variable from our script"
amout_of_cheese = 10
amout_of_crackers = 20

cheese_and_crackers(amout_of_cheese, amout_of_crackers)

print "We can give the expresion"
cheese_and_crackers(10 + 10, 20 + 20)

print "We can use numbers and math expression together"
cheese_and_crackers(amout_of_cheese + 10, amout_of_crackers + 80)
