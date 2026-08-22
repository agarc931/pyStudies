def apply_discount(price, discount):

    # check that the price is an integer or a float
    if isinstance(price, int) or isinstance(price, float):

        # check that the discount is an integer or a float
        if isinstance(discount, int) or isinstance(discount, float):

            # The price must be greater than 0
            if price <= 0 :
                return "The price should be greater than 0"
            
            # The discount should be between 0 and 100
            if discount < 0 or discount > 100 :
                return "The discount should be between 0 and 100"
            
            # calculate the discount
            discount = (price * discount)/100
            total = price - discount

            # print the new price.
            return total

        else:
            # if the discount is not a number
            return "The discount should be a number"
    else:
        # if the price is not a number
        return "The price should be a number"

# test
print(apply_discount(100, 20)) # 80
print(apply_discount(200, 50)) # 100
print(apply_discount(50, 0)) # 50
print(apply_discount(50, 100)) # 0
print(apply_discount(74.5, 20.0)) # 59.6
print(apply_discount("a","b")) # gets error message

