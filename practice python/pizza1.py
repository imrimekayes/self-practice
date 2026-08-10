# start
total_pizzas = 0
total_friends = 0
orders = int(input('number of orders: '))
if orders == 0:
    print('no pizza tonight')
for order in range(1, orders + 1):
    friends = int(input('how many friends? '))
    slices = int(input('how many slices? '))
    pizza_each = slices//friends
    if slices%friends == 0:
        print ('perfect split')
        print ('pizza each',pizza_each)
        total_pizzas += slices
        total_friends += friends
    else:
        slice_left = slices%friends
        print ('pizza each', pizza_each)
        print ('slice left for the dog', slice_left)
        total_pizzas += slices
        total_friends += friends
    print ('total pizzas', total_pizzas)
    print ('avarege', total_pizzas/total_friends)
# stop
