# coding=utf-8

import cherrypy,commands,os,urllib2,DBOperatorWithPool as DBO
db = DBO.DBOperator( 'xiaoyang' , 10, '127.0.0.1', 'root', 'P@ssw0rd', 'xiaoyang' )
class get_ticket:
    def updateRecord( self, db, value1, value2, value3, value4, ):
        value1 = db.escapeString( value1 )
        value2 = db.escapeString( value2 )
        value3 = db.escapeString( value3 )
        value4 = db.escapeString( value4 )
        sql = "update piao set yesno = '%s' where qidian = '%s' and zhongdian = '%s' and date = '%s' " % (value4, value1, value2, value3)
       # print sql
        db.execute( sql )


#updateRecord( db, var1, var2, var3, var4 )
    @cherrypy.expose
    def do_you_have_ticket(self,time,from_station_telecode,to_station_telecode):

#create ticket info        
        ticket_info = "https://dynamic.12306.cn/otsweb/order/querySingleAction.do?method=queryLeftTicket&orderRequest.train_date="+time+"&orderRequest.from_station_telecode="+from_station_telecode+"&orderRequest.to_station_telecode="+to_station_telecode+"&orderRequest.train_no=&trainPassType=QB&trainClass=QB%23D%23Z%23T%23K%23QT%23&includeStudent=00&seatTypeAndNum=&orderRequest.start_time_str=00%3A00--24%3A00"
#get response
        response = urllib2.urlopen(ticket_info)
#put response to original info
        original_info = response.read()
        response.close()
#check ticket_info
       # ticket_info_is = "ticket_info_is "+ticket_info
       # print ticket_info_is
#check original info
       # original_info_is = "original_info_is"+original_info
       # print original_info_is
#change original info to relust

    #put into result file
        result_html = "/var/www/html/results/"+time+from_station_telecode+to_station_telecode+".html"
        result_html_is = "result_html_is"+result_html
       # print result_html_is
        f=open(result_html,'w') # open
        f.write(original_info,) # write
        f.close() #close


    
    #awk original info
    #count str
        k = original_info.count(',', 0)
        #k_is = "k is "+k
        #print "k is"
        #print k
    #get awk num
        def awk_num(start, end):
            step = []
            for i in range (0,10):
                step.append(1)
            step.append(6)
            ret = []
            cnt = 0
            while start <= end:
                ret.append(start)
                start += step[cnt%11]
                cnt += 1
            return ret


        awk_num_out = awk_num(6,k)
    #do awk and grep
        clear = "rm -f /var/www/html/results/testfile.txt"
        os.system(clear)
        for i in awk_num_out:
            awknum = str(i)
            awk="cat "+result_html+"|awk -F, "+"'{print $"+awknum+"}' >> /var/www/html/results/testfile.txt"
 #           print awk
            os.system(awk)
#grep <html>
        sed = '''sed "s/<font color='darkgray'>//g" /var/www/html/results/testfile.txt |sed 's/<\/font>//g' |sed "s/<font color='#008800'>//g" |grep -v \\- > /var/www/html/results/test3.txt ''' 
        os.system(sed)
         
        line_yes = "yes"+"\n"
        clear_yes = '''echo "" > /var/www/html/results/yes.txt'''
        os.system(clear_yes)
        clear_yes_original = '''echo "" > /var/www/html/results/yes_original.txt'''
        os.system(clear_yes_original)
        yesno = open('/var/www/html/results/test3.txt')
        yes_1 = "0"
        for line in yesno:
            line = line.strip()
            if line == "无":
                pass
            else:
#                print "good"
                yes = open('/var/www/html/results/yes.txt','a') #open 
                yes_original = open('/var/www/html/results/yes_original.txt','a')
                line_n = line+"\n"

                yes_original.write(line_n,) # write
                yes.write(line_yes,)

                yes.close() #close
                yes_original.close()
                
                yes_1 = "1"
        self.updateRecord( db, from_station_telecode, to_station_telecode, time, yes_1 )
                
        yesno.close()
        



	#return original info
       # return original_info

#cherrypy.config.update({'server.socket_port':8053})
#cherrypy.config.update({'server.socket_host':'10.32.74.217','server.socket_port':8053})
#cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':8053})
#cherrypy.quickstart(get_ticket())

