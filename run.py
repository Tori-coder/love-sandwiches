# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input
    """
    while True:
        print("Please enter sales data from the last market")
        print("Data should be six numbers, separated by commas")
        print("Ex: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("data is valid\n")
            break

def validate_data(values):
    """
    Inside the try, converts all strs to ints
    Raises value error if strs cannot be converted or if there are not exactly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values)!=6:
            raise ValueError(f"Exactly 6 values required; you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        print("\n")
        return False

    return True

data = get_sales_data()

