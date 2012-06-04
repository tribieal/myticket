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


awk_num_out = awk_num(6,100)
for i in awk_num_out:
    print i
