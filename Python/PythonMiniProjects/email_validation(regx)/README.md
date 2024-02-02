# Email Validation

A simple Python program that validates an email address using basic conditional checks.

## Functionality

- Prompts the user to enter an email address.
- Checks the email address for various conditions to determine its validity.
- Displays specific error messages based on the validation results.

## Usage

1. Run the program using Python.
2. The program will prompt you to enter an email address.
3. Enter the email address you want to validate.
4. The program will check the email address against multiple conditions.
5. If the email address passes all the validation checks, it will be considered valid.
6. If any validation condition fails, the program will display an appropriate error message indicating the reason for the failure.
7. After displaying the error message, the program will terminate.

## Requirements

- Python 3.x

## Example

```
Enter your Email: user@example.com
```
Output:
```
Email is valid.
```

```
Enter your Email: abc@def@ghi.com
```
Output:
```
Invalid email address: Multiple "@" symbols found.
```

```
Enter your Email: example@domain
```
Output:
```
Invalid email address: No top-level domain specified.
```

## License

Feel free to modify and use this code according to your needs.

## Author

MEET LIMBANI

## Acknowledgments

- Inspired by the desire to create a simple email validation program.
