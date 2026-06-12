try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("10 divided by", number, "is", result)

except ValueError:
    print("Error: That was not a number!")

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

print("Program finished.")