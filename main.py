class employee:

    def __init__(self):
        print("employee hired")

    def __del__(self):
        print("destructor called, emloyee fired")

obj = employee()
del obj