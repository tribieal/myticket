#awk original info
    #count str
        k = result_html.count(',', 0)
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
    #do awk
        for i in awk_num_out:
            awknum = str(i)
            awk="cat "+result_html+"|awk -F, "+"'{print $"+awknum+"}' > /var/www/html/results/testfile.txt"
            print awk
            os.system(awk)
