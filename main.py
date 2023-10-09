from sys import set_int_max_str_digits
from fibonacci import fibonacci

def main():
    set_int_max_str_digits(10**7)
    n = int(input("Enter the term of fibonacci you want to find: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()
