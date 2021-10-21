alpha = "I like old music"
password = "K34jndnks"
number_string = "12345"
tabbs = "       "
titles = "I Love Cups"
false_titles = "I love Cups"

print(alpha.isalpha())
print(password.isalnum())
print(number_string.isdecimal())
print(tabbs.isspace())
print(titles.istitle())
print(false_titles.istitle())


# print out u users name and age
name = "James"
age = 19

print("My name is " + name + " I am " + str(age) + " years old")

greetings = 'Hello, Moringa!'

part_one = greetings[0:5]
print(part_one)

greetings = 'Hello, Moringa!'

part_one = greetings[-15:-10]
print(part_one)
part_one = greetings[0:]
print(part_one)
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
four_digits = number[:4]
print(four_digits)


def fun_a():
    print("I have been called")


fun_a()


def fun_a(a, b):
    print(a + b)


fun_a(1, 4)
# Empty function
def fun_afgj():
    print('ma')


    fun_afgj()


def fun_a():
    pass
  