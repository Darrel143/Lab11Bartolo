# Get the number of rows from the user
n = int(input("Enter the number of rows: "))

# Initialize the starting number to the first odd number
num = 1

# Outer loop to handle the number of rows
for i in range(1, n + 1):
    # Inner loop to print numbers in each row
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 2  # Increment by 2 to ensure we get the next odd number
    # Move to the next line after each row
    print()

