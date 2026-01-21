checkEven = lambda No: (No % 2 == 0)

def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if Task(no):
            Result.append(no)
    return Result

def main():
    Data = [10, 11, 12, 13, 14]
    print("Count of Even Numbers:", len(filterX(checkEven, Data)))

if __name__ == "__main__":
    main()
