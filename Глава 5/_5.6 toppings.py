available_toppings = ['mushrooms','olives','green peppers','pepperoni',
    'pineapple','extra cheese']
requested_toppings = ['mushrooms','green peppers','extra cheese','french fries']
#requested_toppings = []
if requested_toppings: # Проверка пустой ли список
    for requested_topping in requested_toppings:
        if requested_topping not in available_toppings:
            pri nt(f"Sorry, we are out of {requested_topping} right now.")
        else:
            print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")
print("\nFinished making your pizza!")
