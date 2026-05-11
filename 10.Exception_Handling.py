try:
    x = int(input("Enter a number: "))
    result = 100 / x
    print(f"Result: {result}")

except ValueError:
    print("That's not a number!")

except ZeroDivisionError:
    print("Can't Divide by zero!")

except Exception as e:
    print(f"Something went wrong: {e}")

finally:
    print("This always runs no matter what")


# Custom Exception

class InvalidYieldError(Exception):
    pass


def validate_yield(yield_kg):
    if yield_kg < 0:
        raise InvalidYieldError(f"Yield cannot be negative: {yield_kg}")

    if yield_kg > 100000:
        raise InvalidYieldError(f"Yield too high to be real: {yield_kg}")

    return True


test_values = [4800, -100, 999999, 3200]

for val in test_values:
    try:
        validate_yield(val)
        print(f"{val} kg - valid")

    except InvalidYieldError as e:
        print(f"ERROR: {e}")