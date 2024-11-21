def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted = (price * discount_percent)/100
        return price - discounted
    else:
        return price
original_price = int(input("Enter the original price: ")) 
discount = int(input("Enter the discount: "))   
    
discounted_price = calculate_discount(original_price, discount)    
print(f"The price is: {discounted_price}")