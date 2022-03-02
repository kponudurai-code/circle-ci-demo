
def add(x, y):
    """Add Function"""
    return x + y

def substract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiple Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

if __name__ == '__main__':
    add(5, 10)
    substract(8, 2)
    divide(10, 0)