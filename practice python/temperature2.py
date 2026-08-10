# start
hottest = None
coldest = None
while True:
    temp = input('enter temperature: ')
    if temp == 'done':
        break
    temp = float(temp)
    if temp >= 30:
        print ('heatwave')
    if 15 < temp < 30:
        print ('nice')
    if 0 < temp <= 15:
        print ('chilly')
    if temp < 0:
        print ('freezing')
    if hottest == None or temp > hottest:
        hottest = temp
    if coldest == None or temp < coldest:
        coldest = temp
if hottest != None and coldest != None:
    print ('hottest temperature' ,hottest)
    print ('coldest temperature' ,coldest)
    spread = hottest - coldest
    print ('spread' ,spread)
else:
    print ('no measurements')
# stop
