square = lambda no: no * no

def main():
    value = 0
    ret = 0

    print("Enter number:")
    value = int(input())

    ret = square(value)
    print("Square is:", ret)

if __name__ == "__main__":
    main()
