checkLen = lambda Str: len(Str) > 5

def filterX(Task, Elements):
    Result = []
    for s in Elements:
        if Task(s):
            Result.append(s)
    return Result

def main():
    Data = ["Python", "Java", "Angular", "C"]
    print("Result:", filterX(checkLen, Data))

if __name__ == "__main__":
    main()
