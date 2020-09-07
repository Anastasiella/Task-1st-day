def format_price(price):
    price = int(price)
    total = "Цена: " + str(price) + " руб."
    return(total)

result = format_price(56.24)

print(result)