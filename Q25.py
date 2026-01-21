Max = lambda A, B: A if A > B else B

def reduceX(Task, Elements):
    MaxVal = Elements[0]
    for no in Elements[1:]:
        MaxVal = Task(MaxVal, no)
    return MaxVal

def main():
    Data = [10, 50, 30, 40]
    print("Result:", reduceX(Max, Data))

if __name__ == "__main__":
    main()
