# start
count = 0
sum_num = 0
max_num = None
min_num = None
code = int(input('entar code'))
if code < 0:
    print ('ignoring minus')
    code = code * -1
elif code == 0:
    count += 1
    min_num = code
    max_num = code
    print (count,sum_num,max_num,min_num)
else:
    while code > 0:
        num = code % 10
        sum_num += num
        count += 1
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num
        code = code // 10
print ('number of digits', count)
print ('sum number', sum_num)
print ('max number', max_num)
print ('min number', min_num)
avarege = sum_num / count
print ('average number', avarege)
if sum_num % 3 == 0:
    print ('lucky')
elif sum_num % 2 == 0:
    print ('even vibes')
else:
    print ('plain')

#stop