balance = 3000
def by_thinigs(item, price):
    global balance
    balance = balance - price
   
    print(f"balance after buying {item} is ", balance)
item = "shoes"
price = 500
by_thinigs(item, price)