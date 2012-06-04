import cherrypy, commands,os,urllib2,DBOperatorWithPool as DBO
class selectAllTable:
    @cherrypy.expose
    def selectAllTable( self, value1, value2, value3 ):
        db = DBO.DBOperator( 'xiaoyang' , 10, '127.0.0.1', 'root', 'P@ssw0rd', 'xiaoyang' )
        value1 = db.escapeString( value1 )
        value2 = db.escapeString( value2 )
        value3 = db.escapeString( value3 )
        sql = "select qidian from piao where qidian = '%s' and zhongdian = '%s' and date = '%s' " % ( value2, value3, value1)
        print sql
        output = db.execute( sql )
#        dir(output)
        c = output.res[0][0]
#        print output.res[0][0]      
# print sql
        print c
        
        return output.res[0][0]


cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':9053})
cherrypy.quickstart(selectAllTable())

#a=selectAllTable()
#a.selectAllTable("2011-12-16", "BXP","XXO")

