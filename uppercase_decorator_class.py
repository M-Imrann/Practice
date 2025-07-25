class UppercaseDecorator():
    '''
    Uppercase decorator class to covert the string into uppercase.
    '''
    def __init__(self, func):
        self.func = func

    def __call__(self):
        result = self.func()
        return result.upper()


@UppercaseDecorator
def greeting():
    return "Hey, I am Muhammad Imran."


print(greeting())
