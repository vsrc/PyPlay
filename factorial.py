import math

# function that returns factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        numbers = range(1, n+1)
        numbers = list(numbers)
        numbers.reverse()
        print (numbers)
        result = numbers[0]
        numbers.pop(0)
        for i in numbers:
            result = result * i

        return result

my = factorial(4)
check = math.factorial(4)

if my == check:
    print("Correct")

else:
    print("Incorrect")


print("my: ", str(my), "check: ", str(check))
