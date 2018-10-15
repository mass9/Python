def apply_discount(product, discount):
    price = int(product['price']*(1.0-discount))
    assert 0 <= price<= product['price']
    return price 
shoes= {'name':'Branded one ' , 'price': 14900}

print(apply_discount(shoes,0.15))
print(apply_discount(shoes,0.25))
print(apply_discount(shoes,0.35))
print(apply_discount(shoes,0.45))
print(apply_discount(shoes,0.55))
print(apply_discount(shoes,0.65))
print(apply_discount(shoes,0.75))
print(apply_discount(shoes,0.85))
print(apply_discount(shoes,0.95))
print(apply_discount(shoes,0.98))
print(apply_discount(shoes,0.99))


