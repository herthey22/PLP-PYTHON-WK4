"""
Create a function named calculate_discount(price, discount_percent)
 that calculates the final price after applying a discount. The function should 
take the original price (price) and the discount percentage 
(discount_percent) as parameters. If the discount is 20% or higher,
 apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the 
original price of an item and the discount percentage. Print the final
 price after applying the discount, or if no discount was applied, print the original price.
 """

#solution

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

original_price = float(input("Enter the original price of the item: #"))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price == original_price:
    print(f"No discount applied. Final price: #{final_price}")
else:
    print(f"Final price after applying {discount_percent}% discount: #{final_price}")
