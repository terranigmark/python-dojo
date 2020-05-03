acre_area_ft = 43560
width = float(input('Input the width of the field: '))
height = float(input('Input the height of the field: '))

area_in_acres = width * height / acre_area_ft

print(f'The area of the field in acres is: {area_in_acres}')