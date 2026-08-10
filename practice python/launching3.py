# start
fuel = float(input('enter the fuel in liters: '))
time = int(input('enter the time in seconds untill launching: '))
count = 0
while time > 0:
    if fuel < 0:
        break
    elif fuel > 0:
        count += 2.5
        fuel -= count
        time -= 1
if fuel > 0:
    print ('lift off! fuel left:', fuel)
else:
    print('out of fuel at', time, 'seconds untill launching')
# stop
