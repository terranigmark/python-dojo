tax = 0.16
tip = 0.1

base_dish_cost = float(input('What is the cost base of the dish: '))

dish_tax = tax * base_dish_cost
dish_tip = tip * base_dish_cost
dish_total_cost = base_dish_cost + dish_tax + dish_tip

print(f'''
The cost of the dish is: ${base_dish_cost:.2f}
The tax added is: ${dish_tax:.2f}
The suggested tip is: ${dish_tip:.2f}

TOTAL: ${dish_total_cost:.2f}
''')