# Question 1
print("Question 1")

def hello_name(user_name):
    """Display user name."""
    print("hello_" + user_name)

hello_name("USERNAME\n")


# Question 2
print("Question 2")

odd_numbers = list(range(1,100,2))
print(str(odd_numbers) + "\n")


# Question 3
print("Question 3")

def max_num_in_list(a_list):
    max = a_list[0]
    for value in a_list:
        if value > max:
            max = value
    return max
print(str(max_num_in_list([4, 70, -50, 99])) + "\n")


# Question 4
print("Question 4")

def is_leap_year(a_year):
    """decides if a year is leap."""
    leap = False
    if a_year % 400 == 0:
        leap = True
    elif a_year % 100 == 0:
        leap = True
    elif a_year % 4 == 0:
        leap = True
    
    return leap

print(str(is_leap_year(1995)) + "\n")


# Question 5
print ("Question 5")

def is_consecutive(a_list):
    """Returns true or false weather or not a list is consecutive numbers."""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

the_list = [1,2,3,4,5,]
print(str(is_consecutive(the_list)) + "\n")
