import pytest
import pandas as pd
import create_database_master.src.duplicates as dup


def test_check_for_duplicates():
    # Test that the function returns True if there are duplicates in the column
    df = pd.DataFrame({'A': [1, 2, 3, 1, 2, 3], 'B': [1, 2, 3, 1, 2, 3]})
    assert dup.check_for_duplicates(df, 'A', column_name2='B') == True

    # Test that the function returns False if there are no duplicates in the column
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [1, 2, 3, 4, 5, 6]})
    assert dup.check_for_duplicates(df, 'A', column_name2='B') == False
