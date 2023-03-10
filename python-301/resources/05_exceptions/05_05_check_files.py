# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    #store the numbers in a list
    num  = []

    with open("resources/05_exceptions/integers.txt", "r") as f:

        for line in f.readlines():
            line = int(line)
            num.append(line)


    first_num = num[0]
    rest_num =num[1:]

    for num in rest_num:
        result = first_num/num
        print(f"{first_num} divided by {num}; ans == {result}")

except ValueError as e:
    print(f"Value Error: {e}")

except FileNotFoundError:
    print("create a new file, file not found")
except ZeroDivisionError:
    print("Divinding by zero is not possible")


finally:
    f.close()


