#The sys module provides variables used or maintained by the interpreter
#Since sys.argv returns a list, we used sys.argv[1] in input_demo.py to retrieve this value
import sys
name = sys.argv[1]

print("How old are you?")
age = int(input())

print(name)
print(age)