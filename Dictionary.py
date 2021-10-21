#Like lists, dictionaries store collections of many values of different
# types. Unlike indexes for lists - which are integers and start from 0,
#  dictionary indexes don't have to be integers.
# They can be of different data types like strings.
# Indexes in dictionaries are called keys.
# The value here is appropriately called the value.


# Creating empty dictionaries
my_dict = {}
my_dict = dict()

# Creating a dictionary with keys and values
my_cat = {'name': 'Mr sniffles', 'age': 18, 'color': 'black'}
cat_name = my_cat['name']
print(cat_name)  # 'Mr sniffles'

birthdays = {"John": "August 1", "Marcus": "April 8"}
birthdays["mary"] = "September 14"
print( birthdays)
print(birthdays.keys())
print(list(birthdays.keys()))
