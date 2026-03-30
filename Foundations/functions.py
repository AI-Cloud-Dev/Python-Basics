
def calculate_area(length, width):
    totalArea = length * width
    print(totalArea)
    return totalArea

calculate_area(10, 5)


def is_even(num):
    if num%2==0:
        print("True")
        return True
    else: 
        print("False")
        return False
    
is_even(10)

def find_fruit(fruit_list, target):
    if target in fruit_list:
        print("Found it")
    else: print("Not Found")

find_fruit(["Apple", "Banana", "Cherry"], "Cherry")

def get_final_price(price, discount_percent):
    discount= price * discount_percent/100
    if price%2==0:
        print("Even price bonus applied!")
        discount+=5
    print(f"Total discount: ${discount}")
    total_price=price-discount    
    print(f"total price : ${total_price}")    
    print(total_price)
    # else: 
    #     print(f"Total discount: ${discount}")
    #     total_price=price-discount    
    #     print(f"total price : ${total_price}")
while True:
    user_price = float(input("Enter the Price"))
    user_discount = float(input("Enter the discount"))
    
    get_final_price(user_price,user_discount)
    
    repeat = input("Calculate another? y/n:")
    if repeat.lower() == "n":
        print("Goodbye!")
        break
        
    
    


# get_final_price(user_price,user_discount)
    