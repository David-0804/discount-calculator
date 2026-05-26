def apply_discount(price:float |  int, discount:float | int):
    if not isinstance(price, (float, int)):
        return "The price should be a number"

    if not isinstance(discount, (float, int)):
        return "The discount should be a number"

    if price <=0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    discount_price = price * (discount / 100)
    return price - discount_price


print(apply_discount(74.5, 20.0))