
# variables
greeting = 'hello'

# methods
print(greeting)
print("world")

# Lists [ ] - have index key
friend_list = ['John', 'Joe', 'Sam', 'Aaron' ]
friend_list.append('Mike')
print(friend_list[0]) # will print John

friend_list[0] = 'James' # replacing John with James
print(friend_list[0]) # will now print James

# Tuples ( ) - immutable
colors = ('blue', 'yellow', 'green')

# can not do my_tuple.append("red"), tuples are immutable
print(colors[1]) # will print yellow

# Sets { } - unordered & unique
europe_countries = { 'UK', 'Sweden', 'Germany' }

# cannot do europe_countries[0] = "Austria", sets are unordered, index key does not exist
# cannot do print(europe_countries[0]), sets are unordered, index key does not exist
# if we do europe_countries.add("uk") we will still have just one element "uk" in set

#  intersection returns set with elements that are same for those two sets
eng_language = { 'UK', 'USA', 'Australia' }
europe_countries.intersection(eng_language) # will return set with only "UK"

# union - returns set with elements from both sets, merge, will discard duplicates
europe_countries.union(eng_language)
# will return set with "UK", "Sweden", "Germany", "USA", "Australia"

# difference - returns set with elements that are different between those two sets
europe_countries.difference(eng_language)
# will return set with "Sweden", "Germany", "USA", "Australia"

days = 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday'
# split takes separator value and splits string whenever that separator value
# occurs and returns list of strings
daysList = days.split(', ')

numbers = [ 3, -1, -100, 25, 9, 77, 33, -100 ]
numbers.sort() # will sort the numbers [-100, -100, -1, 3, 9, 25, 33, 77]
numbers.count(-100) # will output 2 as there is two elements in this list with given param -100

type(daysList) # will output list
'chewsday' in daysList # will output False

# strip removes whitespaces from spring
username = '   joe  '
username = username.strip()
print('user is:' + username)

# for loop iterates through iterables
for friend in friend_list:
	print(friend)

# while condition is true do something
should_run = True
while should_run == True :
	print('I am running!')
        should_run = False

colors_two = colors

# if statement
if colors == days:
	print('tis never ze execute')
elif colors_two == colors:
	print('colors_two and colors are same!')
else:
	colors('this will happen if no previous condition is satisified')

# if - in checks if element is in iterable
if 'joe' in friend_list:
	print('joe is a friend')

# if - not in checks if element is not in iterable
if 'purple' not in colors:
	print('purple is not my color')

# programatically create list of numbers from 0 - 9 and  multiply with two
print([x * 2 for x in range(10)])

# programatically create list of even numbers from 0 - 9
# function comprehension
print([x for x in range(10) if x % 2 == 0])

# split days string into list and then remove whitespace from each element
# and make every element lowercase
print([day.strip().lower() for day in days.split(',')])

# dictionary
student = { "name": "Joe", "age": 21, "grades": [15, 48, 79]}

print(student["name"]) # will print Joe

sequence_numbers = { 1: 32, 2: "three", 3: "7" }
print(sequence_numbers[2]) # will print three

# dictionary that contains string and tuple
lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22)
}

s = sum(lottery_player['numbers'])
print(s)

# list of dictionaries
universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'locatioin': 'US'
    }
]

# dictionary of dictionaries
user = {
    'info': {
        'name': 'Joe',
        'surname': 'Smith'
    },
    'address': {
        'street': 'One Street 245',
        'city': 'London',
        'country': 'UK'
    }
}


class FootballPlayer(object):
    def __init__(self, name, performance):
        self.name = name
        self.performance = performance

    def total(self):
        return sum(self.performance)

    def average(self):
        total = self.total()
        return self.total() / len(self.performance)

    # class method gets cls which is object that called it
    @classmethod
    def who_am_i(cls):
        print(cls)


player1 = FootballPlayer("Rolf", (3, 5, 21, 51))

print(player1.name + ' have an average: ' + str(player1.average()))


# *args unlimited ordered arguments
def get_sum(*args):
    return sum(args)

print(get_sum(5, 7, 3, 14, 2))


# **kwargs unlimited ordered or unordered key-value arguments
def output_all(**kwargs):
    print(kwargs)

output_all(name = 'John', partner = "louise", player = True, wins = 0,
        attempts = 45, age =  "33")


# Class inheritance Python 2.x style
class NewFootballPlayer(FootballPlayer):
    def __init__(self, name, performance, location):
        super(NewFootballPlayer, self).__init__(name, performance)
        self.location = location

    # defining static method, doesn't need any paramethers
    @staticmethod
    def say_hi(person):
        return 'Hi ' + person


player2 = NewFootballPlayer('Jimmy', (3, ), 'London')

print(player2.name + ' is in ' + player2.location)

# both will work as method is defined as static
print(player2.say_hi('Vedran'))
print(NewFootballPlayer.say_hi('World'))

# will print object of class NewFootbalPlayer as that
# is the class of object that called it (player2)
print(player2.who_am_i())


# filter vs function comprehension
my_numbers = range(10)

print('filter with function that we are passing')
def give_me_evens(x):
    return x % 2 == 0
print(list(filter(give_me_evens, my_numbers)))

print('filter with lambda function')
print(list(filter(lambda x: x % 2 == 0, my_numbers)))


print('function comprehension')
print([x for x in range(10) if x % 2 == 0])


# decorators

# import is usually on the top of file
import functools

# define decorator
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator, before the function')
        func()
        print('In the decorator, after the function')

    return function_that_runs_func

# use decorator on function
@my_decorator
def my_function():
    print('i am the one who knocks!')

my_function()



# decorators can accept parameters but are created little bit nested
print('\n\ndecorator with parameters')
def decorator_with_arguments(number):
    def my_decorator_two(func):
        @functools.wraps(func)
        def function_that_runs_func_two(*args, **kwargs):
            print('In the decorator, before the function')

            if number == 56:
                print('You are not right user, not authenticated!')
            else:
                func(*args, **kwargs)

            print('In the decorator, after the function')

        return function_that_runs_func_two
    return my_decorator_two


@decorator_with_arguments(57)
def my_function_two(x, y):
    print(x + y)

my_function_two(3, 5)


# helper for printing out interactive namespace
%whos

# Output something like:

# Variable   Type    Data/Info
# ----------------------------
# a          int     7
# sideA      int     2
# sideB      int     3
# sideC      int     13
