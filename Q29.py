Mul = lambda A, B: A * B

def reduceX(Task, Elements):
    Result = 1
    for no in Elements:
        Result = Task(Result, no)
    return Result

def main():
    Data = [1, 2, 3, 4]
    print("Result:", reduceX(Mul, Data))

if __name__ == "__main__":
    main()
