def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = input('Enter the number: ')
print('Factorial of ' + str(num) + ' is ' + str(factorial(int(num))))