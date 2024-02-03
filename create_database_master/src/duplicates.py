"""
This module checks for duplicates in a dataframe
It is used in the create_database_master/src/duplicates.py module

It checks that two columns together do not have the same values in the same row.


"""

import pandas as pd
import logging
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_for_duplicates(df, column_name1, column_name2):
    # Assuming df is your DataFrame and 'column_name' is the column you're checking
    #print("checking for duplicates")
    duplicates = df.duplicated(subset=[column_name1,column_name2])

    if duplicates.any():
        indices = duplicates[duplicates].index
        logging.info(f"  💩  WARNING: There are duplicates on {indices}.")
        #    print(df[duplicates])
        #    Find indices where Column1 has value1 and Column2 has value2

        return True
    else:
        logging.info(f"  👍🏽  INFO: There are no duplicates.")
        return False



if __name__ == "__main__":
    # Test that the function returns True if there are duplicates in the column
    df = pd.DataFrame({'A': [1, 2, 3, 1, 2, 6], 'B': [1, 2, 3, 1, 2, 6]})
    assert check_for_duplicates(df, 'A', 'B') == True

    # Test that the function returns False if there are no duplicates in the column
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [1, 2, 3, 4, 5, 6]})
    assert check_for_duplicates(df, 'A', 'B') == False
    print("All tests passed!")