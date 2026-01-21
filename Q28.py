checkDiv = lambda No: (No % 3 == 0 and No % 5 == 0)

def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if Task(no):
            Result.append(no)
    return Result

def main():
    Data = [15, 30, 10, 45, 20]
    print("Result:", filterX(checkDiv, Data))

if __name__ == "__main__":
    main()
