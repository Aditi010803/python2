Min = lambda A, B: A if A < B else B

def reduceX(Task, Elements):
    MinVal = Elements[0]
    for no in Elements[1:]:
        MinVal = Task(MinVal, no)
    return MinVal

def main():
    Data = [10, 50, 30, 5]
    print("Result:", reduceX(Min, Data))

if __name__ == "__main__":
    main()
