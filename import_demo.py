print("Enter a string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character,0)
characters[character] = characters[character] + 1

print(characters)

name = "James"
age = 19

print(f"My name is {name} and I am {age} years old")
print('Beyonce\'s lemonade stand')
print(r'Beyonce\'s lemonade stand') #raw string

