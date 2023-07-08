# truthy values
# illustrated by Tom Verguts, July 2023

a = 1
b = 0
if a == 1: # the standard truth test
    print(f"a equals {a}!")

if a:
    print("indeed!")

if len([a]):
    print("I agree too")
    
if b == 0: # another standard truth test
    print(f"but b equals {b}")

if not b:
    print("yep you're right")

if not None:
    print("and this is also printed")
    
if not []:
    print("and even this is acceptable")