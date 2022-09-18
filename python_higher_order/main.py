# a default function to take another function parameter
def spell(text):
    # Making text in upper
    return text.upper()
# Taking text as user input
text = input("Enter a text to print it in uppercase and double: ")
# Spell function with text
print(spell(text))
# Assigning variable with the default function
scream = spell
# Scream with text variable
print(scream(text))
