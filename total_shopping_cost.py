def shopping_cart(cart):
    """Calculate the total cost of items in shopping cart"""
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost

cart = [
        {'name':'Apple','price':0.5,'quantity':4},
        {'name':'Banana','price':0.6,'quantity':3},
        {'name':'Orange','price':0.7,'quantity':5},
        {'name':'Grapes','price':0.4,'quantity':6}
    ]


total_cart = shopping_cart(cart)
print(total_cart)