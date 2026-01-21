div = lambda no: (no % 5 == 0)

def main():
    value = 0
    ret = False

    print("Enter number:")
    value = int(input())

    ret = div(value)

    if ret == True:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()
