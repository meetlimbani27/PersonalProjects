## Calculator Program README

This program is a simple calculator that performs basic arithmetic operations on two numbers based on the user's input.

### Functionality

- The program displays a list of valid operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
  - Modulo (%)

- The user is prompted to enter an operator.

- The user is then prompted to enter the first number.

- The user is prompted to enter the second number.

- The program performs the specified operation on the two numbers and displays the result.

- If the operator is division (/) and the second number is 0, the program displays an error message stating that division by zero is not allowed and terminates.

- If an invalid operator is entered, the program displays an error message stating that the operator is invalid.

### Usage

1. Execute the program.

2. Read the list of valid operations.

3. Enter the desired operator.

4. Enter the first number.

5. Enter the second number.

6. The program will output the result of the operation or an error message, depending on the input.

Note: The numbers entered can be floating-point numbers (decimal numbers).

### Example

```
valid operations are:
1    +
2    -
3    *
4    /
5    %

Enter operator: 3
Enter first number: 5
Enter second number: 2

Result: 10.0
```

```
valid operations are:
1    +
2    -
3    *
4    /
5    %

Enter operator: /
Enter first number: 10
Enter second number: 0

Error: Can't divide by 0
```

```
valid operations are:
1    +
2    -
3    *
4    /
5    %

Enter operator: 6

Error: Invalid operator entered
```

Please note that this README assumes you have Python installed and are familiar with running Python programs from the command line or an integrated development environment (IDE).
