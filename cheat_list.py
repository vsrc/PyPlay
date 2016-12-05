
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
days.split(', ')

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
