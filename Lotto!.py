import random

myNumbers = []
while len(myNumbers) < 7:
    newNumber = random.randint(1,49)

    if newNumber in myNumbers:
        continue

    myNumbers.append(newNumber)

print("Those numbers will win:", myNumbers)