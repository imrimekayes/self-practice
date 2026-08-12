# start
price = 0
payment = 0
shekel: list[int] = [1,5,10,20,50]
product = int(input('choose product between 1-3'))
while True:
    if product > 3 or product < 1:
        product = int(input('choose product between 1-3'))
        continue
    if product == 1:
        price += 7
    if product == 2:
        price += 5
    if product == 3:
        price += 3
    break
while payment < price:
    money = int(input('insert money'))
    if money in shekel:
        payment += money
        continue
    else:
        print ('insert legal amount')
if payment == price:
    print ('exact payment ,enjoy the product')
else:
    change = payment - price
    while change != 0:
        for index in range(len(shekel)-1,-1,-1):
            if shekel[index] <= change:
                change -= shekel[index]
                print ('change left:',change)
                break
    print ('enjoy the product')
# stop
