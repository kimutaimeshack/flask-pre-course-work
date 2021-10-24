'''handle = open("test.txt", "r")

# data = handle.readline()

#data = handle.readlines() #To read many lines we use the readlines() method
data = handle.read()  
print(data)

handle.close()
'''
with open("test.txt", "r") as handle:
    data = handle.read()
    print(data)

# handle = open("test.txt", "r")
# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "memory":
#        counter += 1

# print(counter)


# handle = open("text-write.txt", "w")

# handle.write("Hello Moringa")
# handle.close()
