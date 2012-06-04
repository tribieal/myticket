import cherrypy, commands,os,urllib2
class get_ticket:
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
        ticket_info_is = "ticket_info_is "+ticket_info
        print ticket_info_is
#check original info
        original_info_is = "original_info_is"+original_info
        print original_info_is
#change original info to relust

    #put into result file
        result_html = "/var/www/html/results/"+time+from_station_telecode+to_station_telecode+".html"
        result_html_is = "result_html_is"+result_html
        print result_html_is
        f=open(result_html,'w') # open
        f.write(original_info,) # write
        f.close() #close


    
    #awk original info
    #count str
        k = original_info.count(',', 0)
        #k_is = "k is "+k
        print "k is"
        print k
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
        clear = "echo "" > /var/www/html/results/testfile.txt"
        os.system(clear)
        for i in awk_num_out:
            awknum = str(i)
            awk="cat "+result_html+"|awk -F, "+"'{print $"+awknum+"}' >> /var/www/html/results/testfile.txt"
            print awk
            os.system(awk)
#grep <html>
        sed = '''sed "s/<font color='darkgray'>//g" /var/www/html/results/testfile.txt |sed 's/<\/font>//g' |sed "s/<font color='#008800'>//g" |grep -v \\- > /var/www/html/results/test3.txt ''' 
        os.system(sed)
         
        yesno = open('/var/www/html/results/test3.txt')
        for line in yesno:
            line = line.strip()
            if line == "无":
            else:
                yes = open('/var/www/html/results/yes.txt','a') 
                yes.write(line,) # write
                yes.close() #close
        line.cloud()

	#return original info
        return original_info

#cherrypy.config.update({'server.socket_port':8053})
#cherrypy.config.update({'server.socket_host':'10.32.74.217','server.socket_port':8053})
cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':8053})
cherrypy.quickstart(get_ticket())

