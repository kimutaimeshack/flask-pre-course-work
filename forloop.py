#We can also use a Python function named range() in our for loops. The range()function returns a list for which we can use to loop through.
#A for loop is used when one wants to repeat something a number of times.
for i in range(0, 7):
    print("I would love " + str(i) + " cookies")
    
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


list_a = list(range(0, 5))
print(list_a)