import math

def calculate_square_root(number):
  """
  Calculates the square root of a given number.

  Args:
    number: The number for which to calculate the square root.

  Returns:
    The square root of the number, or an error message if the input is invalid.
  """
  if number < 0:
    return "Cannot calculate the square root of a negative number."
  else:
    return math.sqrt(number)

if __name__ == "__main__":
  try:
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print("The square root of", num, "is", result)
  except ValueError:
    print("Invalid input. Please enter a number.")