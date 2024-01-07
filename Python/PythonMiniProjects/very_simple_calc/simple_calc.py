import sys
print("\nvalid operations are:\n1    +\n2    -\n3    *\n4    /\n5    %")

op = input("Enter operator:")

in1 = float(input(("enter first number:")))
in2 = float(input(("enter second number:")))

match op:                                 
    case "+" | "1":
        print (in1 + in2)
    case "-" | "2":
        print (in1 - in2)
    case "*" | "3":
        print (in1 * in2)
    case "/" | "4":
        if in2 == 0:
            print("can't divide by 0")
            sys.exit()
        print (in1 / in2)
    case "%" | "5":                                   
        print (in1 % in2)
    case _:
        print("invalid operator entered")
