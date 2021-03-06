#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    import sys
    if len(sys.argv) - 1 == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            print(sys.exit(0))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            print(sys.exit(0))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            print(sys.exit(0))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            print(sys.exit(0))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(sys.exit(1))
