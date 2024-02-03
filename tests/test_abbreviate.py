import pandas as pd
import pytest
import create_database_master.src.excel_io_dataframe as xl
import create_database_master.src.abbreviate as ab
@pytest.fixture
def data_base():
    # read instrument Database lists|/
    file_path = '../data/generated_database_v6.0.xlsx'  # Replace this with the path to your workbook 1
    data_base = xl.read_workbook(file_path, -1, 0)
    return data_base


def test_abbreviate(data_base):

    x=ab.abbreviate_text(data_base, 'System', '../Data/ContactEnergy_abbreviations.xlsx')
    assert x.at[571, 'System'] == 'SEP PLT ACID DOSG SEAL WTR'
    assert x.at[0, 'System'] == 'WELLPAD TH11 COM STM/WTR DUMP SYS'


