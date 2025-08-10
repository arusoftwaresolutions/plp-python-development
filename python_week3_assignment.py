def calculate_discount(price, discount_percent):
    """takes the price and returns the price by applying the discount"""
    if discount_percent >=20:
        money_to_reduce=price*(discount_percent/100)
        price-=money_to_reduce
        
        return f" {price} is the new price"
    else:
        return "sorry the discount is below 20 i can't calculate the discount"
    
price = float(input("enter the orginal price "))
discount = float(input("enter the dicount percent "))
print(calculate_discount(price, discount))
