# my_module.py

def fibo(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def palindrome(s):
    """Checks if the given string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def length(s):
    """Returns the length of the given string."""
    return len(s)

def main():
    while True:
        print("\nMenu:")
        print("1. Fibonacci")
        print("2. Palindrome")
        print("3. Length")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            n = int(input("Enter a positive integer: "))
            print(f"Fibonacci({n}):", fibo(n))

        elif choice == '2':
            s = input("Enter a string: ")
            if palindrome(s):
                print(f'"{s}" is a palindrome.')
            else:
                print(f'"{s}" is not a palindrome.')

        elif choice == '3':
            s = input("Enter a string: ")
            print(f'Length of "{s}":', length(s))

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

