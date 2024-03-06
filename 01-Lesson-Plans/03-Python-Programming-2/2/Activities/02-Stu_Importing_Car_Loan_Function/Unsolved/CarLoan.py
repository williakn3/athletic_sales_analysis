""" Calculating the cost of a new car"""

def calculate_future_value(current_loan_value, annual_interest_rate, months_remaining):
    """
    Create a function called calculate_future_value
    Args:
        current_loan_value (float): The current loan value
        the annual_interest_rate (float): The APR
        the months_remaining (int): The number of months remaining on the loan

    Returns:
        Prints the future value of the loan as a float.
    """
    future_value = current_loan_value * (1 + (annual_interest_rate / 12)) ** months_remaining
    # Print the future value of the car to 2 decimal places.
<<<<<<< HEAD
    return future_value
=======
    return future_value
>>>>>>> e9bf0776dd9a5784f4249f28b06a95e85d026700
