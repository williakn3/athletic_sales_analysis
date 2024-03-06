"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.
"""

accounts = [
    {
    "pin": 123456,
<<<<<<< HEAD
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3258.42}
=======
    "balance" : 1436.19
    },
    {
    "pin" : 246802,
    "balance": 3571.87
    },
    {
    "pin": 135791,
    "balance" : 543.79
    },
    {
    "pin" : 123987,
    "balance": 25.89
    },
    {
    "pin" : 269731,
    "balance": 3258.42
    }
>>>>>>> e9bf0776dd9a5784f4249f28b06a95e85d026700
]

# Define the `login` function for the ATM application.
def login(pin):
    """Create a login function for the ATM application.
    Args:
        pin (integer): The users pin number

    Returns:
        If the pin matches one of the pin numbers in the "accounts"
        the account balance is returned.

    Notes:
        Create a for loop to check to validate the PIN against this list of `accounts`.
        If the PIN is validated, print the account's balance formatted to two decimal places and thousandths.
    """
<<<<<<< HEAD
    for account in accounts:
        if int(pin) == account["pin"]:
            print(f"The account balance for PIN {account['pin']} is: ${account['balance']: ,.2f}.")
=======
    for acct in accounts:
        if int(pin) == acct["pin"]:
            print(f"The account balance for PIN {acct['pin']} is: ${acct['balance']: ,.2f}.")
>>>>>>> e9bf0776dd9a5784f4249f28b06a95e85d026700


if __name__ == "__main__":
    # Set the function call equal to a variable called account_balance.
    account_balance = login(246802)
