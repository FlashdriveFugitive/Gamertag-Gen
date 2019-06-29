import random
random.randint (0,10)

adjectiveList = ["Happy", "Sugar", "Nvidia", "Wooden", "Mental", "Embarrassed", "Kangaroo", "Cat", "Ghost", "Able", "Solider", "AMD", "Robot", "Computer", "Coder", "Software", "Engineer",]

colorList = ["Black", "Red", "Blue", "Green", "Orange", "Yellow"]

genderList = ["Boy", "Girl"]

designList = ["xX", "Xx", "oO", "Oo", "AK","xo"]

pickedList = []

if random.choice ([True, False]):
  pickedList = colorList
else:
  pickedList = genderList

first = random.choice(adjectiveList)

middle = random.choice(pickedList)

last = random.randint (1,9)

design = random.choice (designList)

designReversedAsList = list(design)
designReversedAsList.reverse()

print ("Gamertag Generator")

print (design + first +"_"+ middle + str(last) + "".join(designReversedAsList))
