import DBOperatorWithPool as DBO
def updateRecord( db, value1, value2, value3, value4, ):
    value1 = db.escapeString( value1 )
    value2 = db.escapeString( value2 )
    value3 = db.escapeString( value3 )
    value4 = db.escapeString( value4 )
    sql = "update piao set yesno = '%s' where qidian = '%s' and zhongdian = '%s' and date = '%s' " % (value4, value1, value2, value3)
    print sql
    db.execute( sql )


db = DBO.DBOperator( 'xiaoyang' , 10, '127.0.0.1', 'root', 'P@ssw0rd', 'xiaoyang' )
#var1 = "BXP"
#var2 = "XXO"
#var3 = "2011-12-16"
#var4 = "0"
#updateRecord( db, var1, var2, var3, var4 )
