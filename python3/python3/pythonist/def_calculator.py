def calc(a, b, operation):
    
    result = 'Операция не поддерживается'
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a + b
    elif operation == '/':
        if b is not 0:
            result = a / b
            
    return result

if __name__ == '__main__':
    print(calc(30, 15, '+'))
    print(calc(30, 15, '-'))
    print(calc(30, 15, '*'))
    print(calc(30, 15, '/'))