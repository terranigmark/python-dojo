import pyperclip

PLAIN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
CYPHER = 'ZYXWVUTSRQPONMLKJIHGFEDCB '

output_text = ''
input_text = input("Write your message: ")

for character in input_text.lower():
    if character in PLAIN:
        position = PLAIN.index(character)
        output_text += CYPHER[position]

print(output_text)

pyperclip.copy(output_text)