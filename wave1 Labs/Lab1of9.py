# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
#and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

#capitalize sentence,
statement = "this will be capitalized"
print(statement)

new_statement = statement.capitalize()
print(new_statement)

#casefold
statement = "THIS WILL BE LOWER CASE"
print(statement)
new_statement = statement.casefold()
print(new_statement)

#count
string = "this is the first virtual internship by wejapa, it is really great to be part of the first intake"
new_string = string.count('the')
print(string)
print(new_string)

#find
print(string.find('internship'))