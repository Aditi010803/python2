checkEven = lambda no: (no % 2 == 0)

def main():
    value = 0
    ret = False

    print("Enter number:")
    value = int(input())

    ret = checkEven(value)

    if ret == True:
        print("It is Even")
    else:
        print("It is Odd")

if __name__ == "__main__":
    main()
