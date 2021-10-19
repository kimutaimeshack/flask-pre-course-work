#We can also use a Python function named range() in our for loops. The range()function returns a list for which we can use to loop through.
#A for loop is used when one wants to repeat something a number of times.
for i in range(0, 7):
    print("I would love " + str(i) + " cookies")



list_a = list(range(0, 20))
for i in list_a:
    if i % 2 == 0:
        print(i)