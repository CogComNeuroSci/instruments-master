##################
## Dictionaries ##
##################

## Dictionaries have an easy setup
## They are contained using curly brackets {}
## All items within the dictionary are separated by commas. 
## An item consists of a key and a value
## These values can be called by their corresponding key.
## For example, we can define a key called 'Function', and when we print 'dictionary["Function"]', we will see the value associated
## to that key.
## In this case, we will see 'Student', as the item 'Function': 'Student' was defined in the dictionary
## Of course, we cannot call items that are not defined in the dictionary
## To illustrate, we try to print what is stored in the key 'University'
## Uncomment to see what happens

dictionary = {"Function": "Student", "Age": 21, "Bachelor": 3}
print(dictionary)

print("Function: ", dictionary["Function"])
print("Age: ", dictionary["Age"])
## print("University: ", dictionary["University"])

## To update a dictionary, we simply link a new value with the key 

dictionary["Age"] = 22
dictionary["School"] = "Ghent University"

print("Age: ", dictionary["Age"])
print("School: ", dictionary["School"])

## When you don't need the items in the dictionary anymore, you can do some operations to delete items in the dictionary
## Alternatively, you can also delete the entire dictionary  using a simple operation
    ## To remove a specific entry, we can use the del() function
    ## To remove all entries in a dictionary, we can use clear()
        ## The print will yield an empty dictionary, visualized by '{}'
    ## To remove the entire dictionary, we can also use del()
        ## The final print statement will yield a NameError, as 'dictionary' will be seen as undefined
            ## This is of course the case because the dictionary was deleted 
## Specific examples of each implementations can be seen below

del(dictionary["School"])
print(dictionary)

dictionary.clear()
print(dictionary)

del(dictionary)
##print(dictionary)

## Dictionaries have some advantages, however, there are also some major disadvantages
## An example is the issue with the definition of the name of the keys
## To illustrate, we define a dictionary which has 'school' two times as a Key name in it
    ## When this is the case, the last definition wins
    ## In the code below for example, the value 'Stark' is the last variable assigned to the key 'Name'
    ## Therefore, this is the value that is printed when the key 'Name' is called

dictionary = {"Name": "Bran", "Name": "Stark", "Call": "Winter is coming"}

print("Name: ", dictionary["Name"])

## A last remark is that the names of the keys must consist of immutable (unchangeable) objects
## Because of this property, the names of the keys must be a string, integer or a tuple
## When the key name is a list (which is mutable), an error will be issued
## We provide an example below to illustrate 
    ## As the name of the key is a list, the following error will occur
        ## TypeError: unhashable type: 'list'
        ## Uncomment to see for yourself

dictionary = {"First name": "Bran", "Last name": "Stark", "Call": "Winter is coming"}
print(dictionary)

WrongKeyName = ["First name"]
print(type(WrongKeyName), WrongKeyName)

## dictionary_error = {WrongKeyName: 'Bran', 'Last name': 'Stark', 'Call': 'Winter is coming'}
## print(dictionary_error)

## That were the main remarks on dictionaries
## We note that other functions still are available
## We provide a short rundown on some of the most eminent functions

## Get an overview of all the keys and what value is stored in the key
## Returns pairs of the keys and their associated value

print(dictionary.items())

## Get an idea about the keys you defined in your dictionary
## No associated values are printed here

print(dictionary.keys())

## To get an idea about the values we have in the dictionary, we can use the function values()

print(dictionary.values())

## Of course, other functions are available
    ## We encourage to discover these for yourself
## When in doubt about properties/functions of dictionaries
    ## Google is your friend!

#########
## END ##
#########