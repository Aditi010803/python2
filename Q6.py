checkOdd = lambda no: (no % 2 != 0)

def main():
    value = 0
    ret = False

    print("Enter number:")
    value = int(input())

    ret = checkOdd(value)

    if ret == True:
        print("It is Odd")
    else:
        print("It is Even")

if __name__ == "__main__":
    main()
