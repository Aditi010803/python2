Add = lambda A, B: A + B

def reduceX(Task, Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum, no)
    return Sum

def main():
    Data = [10, 20, 30]
    print("Result:", reduceX(Add, Data))

if __name__ == "__main__":
    main()
