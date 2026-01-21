maximum = lambda a, b: a if a > b else b

def main():
    no1 = 0
    no2 = 0
    ret = 0

    print("Enter first number:")
    no1 = int(input())
    print("Enter second number:")
    no2 = int(input())

    ret = maximum(no1, no2)
    print("Maximum number is:", ret)

if __name__ == "__main__":
    main()
