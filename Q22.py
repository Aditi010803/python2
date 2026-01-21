checkEven = lambda No: (No % 2 == 0)

def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if Task(no):
            Result.append(no)
    return Result

def main():
    Data = [1, 2, 3, 4, 5, 6]
    print("Result:", filterX(checkEven, Data))

if __name__ == "__main__":
    main()
