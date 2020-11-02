# Program #1 - Hello World
# print("Hello World")

# Drawing a Shape to console
# runs in order. Top down, order of instructions matter
print("Drawing Shapes:")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("")

# Variables and Datatypes
# Save name and age in a variable
# https://www.w3schools.com/python/python_datatypes.asp
print("Variables and Datatypes: ")
character_name = "Mads" # string datatype, plain txt
character_age = "30"
print("There once was a man " + character_name + ",")
print("he was " + character_age + " years old,")
# update the variables
character_name = "Mike"
character_age = "40"
print(character_name + " liked his name, but not being his age, which was " + character_age)
print("")

# Working with strings
print("Working with Strings")
# Insert newline \n
print("Hello\nWorld")
# Insert " " in a print
print("This is a qutation \" this is a backlash \\ ")
# Printing a variable
variable_string = "THIS is a string, contained in a variable"
print(variable_string)
# Concatination of string
print(variable_string + " + concattenatted string")
# convert to lowercase
print(variable_string.lower() + " + lowered")
print(variable_string.upper() + " + upper")
# functions
print(variable_string.upper().isupper()) # Returns a boolean
print(len(variable_string)) # Returns length of string
# Get i index from the string, python is 0 index
print(variable_string[0]) # Returns T
print(variable_string[8]) # return a, whitespace is also in index.
# Get index number of a char. Will throw error if cannot find it.
print(variable_string.index("a"))
print(variable_string.index(" ")) # first whitespace it finds
print(variable_string.index("is")) # tells where it starts
# Replace
print(variable_string.replace("THIS", "Here"))


