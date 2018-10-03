number = 0
while True:
    print(number)
    number += 1
    if number == 20:
        break

for number in range(10):
    if number%2 == 0:
        continue
    print(number)

for letter in "Spell this": 
   if letter != " ":
      pass
   else:
      print("The space came right after this letter!")
   print("Letter :" + letter)