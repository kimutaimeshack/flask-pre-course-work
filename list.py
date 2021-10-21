# can join two lists using the extend() method.
list_a = ["a", "b", "c", "d"]
list_b = [7,9,1, 2, 3, 4, 5, 6]

list_a.extend(list_b)
list_a.append("e")
list_a.reverse()
list_b.sort()

print(list_a)  # this will print ["a","b","c","d",1,2,3,4,5,6]
print(list_a)  # this will print [1,2,3,4,5,6]
print(list_b)