import DBOperatorWithPool as DBO
def newRecord( db, value1, value2, value3, value4, ):
    value1 = db.escapeString( value1 )
    value2 = db.escapeString( value2 )
    value3 = db.escapeString( value3 )
    value4 = db.escapeString( value4 )
    sql = "insert into piao (qidian,zhongdian,date,yesno)values('%s','%s','%s','%s') " % (value1, value2, value3, value4)
    print sql
    db.execute( sql )


db = DBO.DBOperator( 'xiaoyang' , 10, '127.0.0.1', 'root', 'P@ssw0rd', 'xiaoyang' )

var3 = "2011-12-16"
var4 = "0"
f = open('name.txt')
g =f.readlines()

for i in g:
	for j in g:
                var1=i.strip()
                var2=j.strip()
                newRecord( db, var1, var2, var3, var4 )



