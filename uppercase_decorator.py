def uppercase_decorator(func):
    '''
    Uppercase decorator class to covert the string into uppercase.
    '''
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def greeting():
    return "Hey, I am Muhammad Imran."


print(greeting())
