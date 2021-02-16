# Count strings in a sentence
# Count lower case and uppercases
# Converting of strings
string = 'To construct the notion of a Lie group in Dirac geometry, extending the definition of Poisson Lie groups, the Courant algebroids A must themselves carry a multiplicative structure.'
newstring = ' '  
count_upperCase = 0
count_lowerCase = 0
count_blankspace = 0

#total length of sentence
totalLen = len(string)

#half length of sentence
halfString = totalLen/2

#for loops
for letter in string:  
# Checking for lowercase letter and  
# converting to uppercase.  
    if (letter.isupper()) == True:  
        count_upperCase+= 1
        newstring+=(letter.lower())  
        
# Checking for uppercase letter and 
# converting to lowercase.  
    elif (letter.islower()) == True:  
        count_lowerCase+= 1
        newstring+=(letter.upper())
        
# Checking for whitespace letter and 
# adding it to the new string as it is.
    elif (letter.isspace()) == True:  
        count_blankspace+= 1
        newstring+= letter 
        
totalChar = count_upperCase + count_lowerCase + count_blankspace

print("String: \n To construct the notion of a Lie group in Dirac geometry, extending the definition of Poisson Lie groups, the Courant algebroids A must themselves carry a multiplicative structure.")  
print("\n Total Length - ", totalLen)
print("\n Total Characters Length - ", totalChar)
print("\n Uppercase - ", count_upperCase)
print("\n Lowercase - ", count_lowerCase)  
print("\n Spaces -", count_blankspace)
print("\n Converted String:")  
print(newstring)
print(halfString)
