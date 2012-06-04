a = "有"
c = open('c.txt', "r")
n = c.read()

for d in n:
    if a == d:
        print "yes"
    else:
        print "no"
    
