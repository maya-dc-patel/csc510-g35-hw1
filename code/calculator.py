def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def divide(a, b):
    if b==0:
        print('No operation')
        return 0
    return a/b
'''
def main():
    a= int(input('Enter a: '))
    b= int(input('Enter b: '))
    ops= input('Enter the operation you want to perform: ')
    if ops=='+':
        x= addition(a, b)
    if ops=='-':
        x= subtraction(a, b)
    if ops=='*':
        x= multiplication(a, b)
    if ops=='/':
        x= divide(a, b)
    print('Your Result is ',x)
if __name__=='__main__':
    main()
'''