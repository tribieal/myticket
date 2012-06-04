import cherrypy, commands,os
class HelloWorld:
    @cherrypy.expose
    def give_record(self,name,ip):
        record = "\n"+name+"           IN A            "+ip
#del record if exist        
        cmd="sed '/"+name+"/d' < /var/named/chroot/var/named/xingcloud.com.zone > /var/named/chroot/var/named/xingcloud.com.zone.tmp; cat /var/named/chroot/var/named/xingcloud.com.zone.tmp > /var/named/chroot/var/named/xingcloud.com.zone"
        os.system(cmd)
# change zone file 
        f=open('/var/named/chroot/var/named/xingcloud.com.zone','a') # open
        f.write(record,) # write
        f.close() #close


#        import commands
        commands.getstatusoutput('/etc/init.d/named restart')

        return record
#cherrypy.config.update({'server.socket_port':8053})
cherrypy.config.update({'server.socket_host':'10.32.74.217','server.socket_port':8053})
#cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':8053})
cherrypy.quickstart(HelloWorld())

