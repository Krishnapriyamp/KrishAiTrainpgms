def checkprime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

# Input range from user
low = int(input("Enter the start of range: "))
high = int(input("Enter the end of range: "))

print(f"Prime numbers between {low} and {high} are:")
for num in range(low, high + 1):
    if checkprime(num):
        print(num, end=" ")
1