import pyperclip

PLAIN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?!'

output_text = ''
input_text = input("Write your message: ")

option = input("Cypher or Decypher (C/D)?: ")
grade = int(input("Number of positions (1-25): "))

for character in input_text.upper():
    if character in PLAIN:
        position = PLAIN.find(character)
        if option.lower() == 'c':
            position = (position + grade) % 26
        elif option.lower() == 'd':
            position = (position - grade) % 26

        output_text += PLAIN[position]

    else:
        output_text += character

print(output_text)

pyperclip.copy(output_text)
3057047152
