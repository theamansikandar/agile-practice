import sys
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def product(a,b):
    return a*b
def divide(a,b):
    result = a / b if b != 0 else None
    return result

if __name__=='__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    result = divide(a, b)
    if result is not None:
        print(f"Result: {result}")
    else:
        print("Error: Division by zero is not allowed.")