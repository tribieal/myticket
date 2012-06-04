import DBOperatorWithPool as DBO

var3 = "2011-12-16"
f = open('name.txt')
g =f.readlines()

for i in g:
	for j in g:
                var1=i.strip()
                var2=j.strip()
                c = '''get_ticket().do_you_have_ticket(\"'''+var3+'''\",\"'''+var1+'''\",\"'''+var2+'''\")'''
                print c 


# get_ticket().do_you_have_ticket("2011-12-16","BXP","WMR")
