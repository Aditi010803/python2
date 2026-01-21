Square = lambda No: No * No

def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Result.append(Task(no))
    return Result

def main():
    Data = [1, 2, 3, 4, 5]
    print("Result:", mapX(Square, Data))

if __name__ == "__main__":
    main()
