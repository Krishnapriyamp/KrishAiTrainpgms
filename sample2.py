def arithmetic_ops(a, b):
    print("Arithmetic Operators:")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Undefined (division by zero)")
    print("Floor Division:", a // b if b != 0 else "Undefined")
    print("Modulus:", a % b if b != 0 else "Undefined")
    print("Exponent:", a ** b)

def assignment_ops(a, b):
    print("Assignment Operators:")
    x = a
    print(f"intial x value is {x}\n value of b={b} ")
    x += b; print("x += b:", x)
    x -= b; print("x -= b:", x)
    x *= b; print("x *= b:", x)
    x /= b if b != 0 else 1; print("x /= b:", x)
    x //= b if b != 0 else 1; print("x //= b:", x)
    x %= b if b != 0 else 1; print("x %= b:", x)
    x **= b; print("x **= b:", x)

def comparison_ops(a, b):
    print("Comparison Operators:")
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

def logical_ops(a, b):
    print("Logical Operators:")
    print("a > 0 and b > 0:", a > 0 and b > 0)
    print("a > 0 or b < 0:", a > 0 or b < 0)
    print("not(a > b):", not(a > b))

def bitwise_ops(a, b):
    print("Bitwise Operators:")
    print("a & b:", a & b)
    print("a | b:", a | b)
    print("a ^ b:", a ^ b)
    print("~a:", ~a)
    print("a << 1:", a << 1)
    print("a >> 1:", a >> 1)

def identity_ops(a, b):
    print("Identity Operators:")
    print("a is b:", a is b)
    print("a is not b:", a is not b)

def membership_ops():
    print("Membership Operators:")
    my_list = [1, 2, 3, 4, 5, 10]
    num = int(input("Enter number to check in list [1,2,3,4,5,10]: "))
    print(f"{num} in list:", num in my_list)
    print(f"{num} not in list:", num not in my_list)

# Main Program
print("----- Python Operator Menu Program -----")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

while True:
    print("\nChoose an operation:")
    print("1. Arithmetic Operators")
    print("2. Assignment Operators")
    print("3. Comparison Operators")
    print("4. Logical Operators")
    print("5. Bitwise Operators")
    print("6. Identity Operators")
    print("7. Membership Operators")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        arithmetic_ops(a, b)
    elif choice == '2':
        assignment_ops(a, b)
    elif choice == '3':
        comparison_ops(a, b)
    elif choice == '4':
        logical_ops(a, b)
    elif choice == '5':
        bitwise_ops(a, b)
    elif choice == '6':
        identity_ops(a, b)
    elif choice == '7':
        membership_ops()
    elif choice == '8':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
