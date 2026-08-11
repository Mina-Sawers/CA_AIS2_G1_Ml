''' 
Author: Mina

'''

def factorial(num:int)->int:
    ''' 
    calculate n! using Recursion function
    Args:
        num(int): user input the int number
    Return:
        num(int): return the factorial
    Examples:
        factorial(5) = 120
    '''
    if num==0:
        return 1
    return num*factorial(num-1)

def is_prime(num:int)->bool:
    ''' 
    This function check whether the number prime or not

    Args:
        num(int): number to check
    Return:
        bool: True if the number is prime or false ifnot prime
    Examples:
        is_prime(7)->True
    '''
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True