### Dictionaries
BeerPrices = {"Stella": 2.5, "Hoegaarden": 3, "Kriek": 3, "Duvel": 3.5, "Westmalle-dubbel": 3.5, "Westmalle-triple": 3.5}

print(BeerPrices["Hoegaarden"])

print(BeerPrices.keys())
print(BeerPrices.values())

# this line of code won't work
# print(BeerPrices.values()[2])
# this line will tell you why
print(type(BeerPrices.values()))

# converted to a list
BeerPriceList = list(BeerPrices.values())
BeerNamesList = list(BeerPrices.keys())

# check whether the data type is list
print(type(BeerPriceList))
print(type(BeerNamesList))

# Access the information via indices
print(BeerPriceList[0:2])
print(BeerNamesList[0:2])