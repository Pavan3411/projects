def add(n1,n2):
    return n1+n2
def multiply(n1,n2):
    return n1*n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2

n1=int(input("Enter the first number? "))
n2=int(input("Enter the second number? "))
operation=(input("Pick up the operation(+,-,*,/) "))

if operation == "+" :
    answer= add(n1,n2)
elif operation == "*" :
    answer= multiply(n1, n2)
elif operation == "-" :
    answer= subtract(n1,n2)
elif operation == "/" :
    answer= divide(n1, n2)

print(answer)


