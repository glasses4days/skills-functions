# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def print_hello_world():
    """Prints 'Hello World'"""
    print "Hello World"

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def print_user_name(name):
    """Prints name"""
    print "Hi", name

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.
def multiply_integers(x, y):
    """Multiplies x and y then prints the result."""
    print x * y

# 4. Write a function that takes a string and an integer and
#    prints the string that many times
def print_multiple_times(str, int):
    """Prints given string number of times indicated in argument"""
    print str * int

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".
def print_higher_or_lower(num):
    """Checks if higher than,lower than, or equal to 0 and prints result"""
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    elif num == 0:
        print "Zero"

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
def print_divisible_by_three(num):
    """"Checks if num is evenly divisible by 3 and prints True or False"""
    if num%3 == 0:
        print True
    else:
        print False

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.
def count_spaces(sentence):
    """Checks sentence for number of spaces and returns result."""
    counter = 0

    for char in sentence:
        if char == " " :
            counter += 1

    return counter

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def calculate_total_meal_cost(price, tip=15):
    """Calculates meal price with tip. Tip defaults to 15 percent if none given"""
    meal_total = "{0:.2f}".format(price + price * tip/100)
    
    return meal_total

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

def print_sign_parity(num):
    """Checks if num is even or odd and positive or negative and prints result."""
    num_attributes = []
    
    if num % 2 == 0:
        num_attributes.append("Even")
    else:
        num_attributes.append("Odd")
    if num >= 0:
        num_attributes.append("Positive")
    else:
        num_attributes.append("Negative")
    
    
    return num_attributes
    
#unpacks result of calling print_sign_parity and assigns to sign and parity
sign, parity = print_sign_parity(88)
print sign, parity


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
