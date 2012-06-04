import cherrypy, commands,os,urllib2
class get_ticket:
    @cherrypy.expose
    def do_you_have_ticket(self,time,from_station_telecode,to_station_telecode):

#create ticket info        
        ticket_info = "http://127.0.0.1/results/you.html"
#        ticket_info = "https://dynamic.12306.cn/otsweb/order/querySingleAction.do?method=queryLeftTicket&orderRequest.train_date="+time+"&orderRequest.from_station_telecode="+from_station_telecode+"&orderRequest.to_station_telecode="+to_station_telecode+"orderRequest.train_no=&trainPassType=QB&trainClass=QB%23D%23Z%23T%23K%23QT%23&includeStudent=00&seatTypeAndNum=&orderRequest.start_time_str=00%3A00--24%3A00"

#get response
        response = urllib2.urlopen(ticket_info)
#put response to original info
        original_info = response.read()
        response.close()
#check ticket_info
        print ticket_info
#check original info
        print original_info
#change original info to relust

#put into result file
        result_html = "/var/www/html/results/"+time+from_station_telecode+to_station_telecode+".html"
        f=open(result_html,'w') # open
        f.write(original_info,) # write
        f.close() #close

#return original info
        return original_info

#cherrypy.config.update({'server.socket_port':8053})
#cherrypy.config.update({'server.socket_host':'10.32.74.217','server.socket_port':8053})
cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':8053})
cherrypy.quickstart(get_ticket())

