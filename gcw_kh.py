# # Python review function introduction

# ### Problem 1
# Create a ```printNumbers``` function to print integers from -25 to 20 to the console (print in the function)

# define the numbers to print. The method that I thought was best was to use a range with the given integers.
def printNumbers():
    #Range -25 to 20. count up by 1 end at 21 to ensure that 20 is included in the printed count.
    k = range(-25,21,1)
    #starting at -25 add 1 to x until it gets to printed 20.
    for x in k:
        print(x)
#call the function
printNumbers()






# ### Problem 2
# Create a function called checkPassword. Send two string variables to the checkPassword function to check if the strings are equal. Return true if they are equal and false if they are not equal. Print the function's return value.
#define password checker
def checkPassword():
    #if the two passwords do not match retrun false otherwise return true.
    if password1 != password2:
        return 'false'
    else:
        return 'true'
#variables created to hold passwords
password1 = input("enter password ")
password2 = input("enter password again for validation ")
#call function
checkPassword()





# ### Problem 3
# Write a function that determines if a number passed to it is odd or even. Pass a number of your choosing (using input a good idea) and then using the result from the function, print if the number was even or not.
#
# examples:
# ```
# The number 12 is an even number!
#
# The number 5 is an odd number!
# ```


#determine if the number is even or odd. create a variable to hold the user number
def evenOodd():
    # if the lucky number is divided by 2 with no remainder it is even otherwise it is odd. print odd when the number is divisible by 2 with remainder. If there is no remainder the number is even.
    if (luckyNumber % 2) == 0:
        print('your number is an even number')
    else:
        print('your number is an odd number')
luckyNumber = int(input("enter a number to determine if even or odd  "))

#call function
evenOodd()


# ### Problem 4
# * Create a function for the challenge that you call from your ```main```
# * Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```) and returns a string using the passed in greeting and 'World' (ex. ```Howdy World!```)
# * From your *first* function, call the function(s) and print out the final result returned

#define first function "challenge". Challenge function is empty and calls second function.
def challenge():
    second_function()
    #second_function passes a portion of the greeting and calls the greeting function.
def second_function ():
    greet1 = 'Howdy'
    greeting(greet1)
    #greeting function receives the greet1 variable and adds string
def greeting (greet1):
    print(f'{greet1} World!')
#call challenge function and print greet1 and World!
challenge()






# ### Problem 5:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
#define exit strategy
def exit():
    #assign user information to a variable
    userData = ""
    #if the userData isn't q keep going until q is received as an input.
    while userData !='q':
        userData = input("enter some junk, but enter q to quit   ")
#call the extit function
exit()






# ### Challenge
# Create a function that accepts 2 numbers. When the function is called return the sum, difference, product, and quotient as 4 separate return values.
#
# Print the 4 results that are returned using f-strings.
#
# Example: If 2 and 6 are passed into the function, output should be similar to the following:
#
# ```
# The sum of 2 + 6 is 8
# The difference of 2 - 6 is  -4
# The product of 2 * 6 is 12
# The quotient of 2 / 6 is .333
# ```
#define the functin to ask the user for some numbers
def askUser(num1, num2):
#the user inputs are passes to num1 and num2. The userResults function is called and the num1 and num 2 parameters are passed.
    userResults(num1, num2)
# define userResults and receive num1 and num2
def userResults(num1, num2):
    #variables for totals (addition, subtraction, multiplication, and division)
    total = num1 - num2
    total1 = num1 + num2
    total2 = num1 * num2
    total3 = num1 / num2
    #print using f strings to give the difference, sum, product, and quotient
    print(f'The difference of: {ask1} minus {ask2} is {total}')
    print(f'The sum of: {ask1} plus {ask2} is {total1}')
    print(f'The product of: {ask1} times {ask2} is {total2}')
    print(f'quotient: {ask1} divided by {ask2} is {total3}')
#create variables for 2 numbers that are intergers
ask1 = int(input("Enter a number "))
ask2 = int(input("Enter another number "))


#Call the function
askUser(ask1, ask2)
