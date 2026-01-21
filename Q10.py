largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

def main():
    no1 = 0
    no2 = 0
    no3 = 0
    ret = 0

    print("Enter first number:")
    no1 = int(input())
    print("Enter second number:")
    no2 = int(input())
    print("Enter third number:")
    no3 = int(input())

    ret = largest(no1, no2, no3)
    
    print("Largest number is:", ret)

if __name__ == "__main__":
    main()
