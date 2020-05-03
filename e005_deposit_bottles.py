small_bottle = 0.1
big_bottle = 0.25

person_small_bottles = float(input('How many small bottles did you bring?: '))
person_big_bottles = float(input('How many big bottles did you bring?: '))

amount_to_pay = (person_small_bottles * small_bottle) + (person_big_bottles * big_bottle)

print(f'''
Your brought {person_small_bottles} small bottles, {person_big_bottles} big bottles.
You earned: {amount_to_pay}
''')