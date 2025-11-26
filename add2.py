def add(x, y):
    return x + y

if _name_ == "_main_":
    import sys
    if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    else:
        num1 = 15
        num2 = 30
    print("Sum:", add(num1, num2))