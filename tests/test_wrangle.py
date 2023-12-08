import pytest

import create_database_master.src.excel_io_dataframe as xl
import create_database_master.src.wrangle_database_master as wr
@pytest.fixture
def database_data():
    #read instrument Database lists|/
    file_path = '../data/database_master_shortList.xlsx'  # Replace this with the path to your workbook 1
    instrument_data_list_df = xl.read_workbook(file_path, -1, 0)
    return instrument_data_list_df

@pytest.fixture
def instrument_data():
    #read instrument master lists|
    file_path = '../data/instrument_master_shortList.xlsx'  # Replace this with the path to your workbook 2
    instrument_master_list_df = xl.read_workbook(file_path, -1, 0)
    return instrument_master_list_df

@pytest.fixture
def wrangle_data():
    instrument_dat = instrument_data
    database_dat = database_data
    wr.wrangle_database_list(instrument_dat, database_dat, version='')

def test_lines_database_master(database_data):
    assert len(database_data) == 6
def test_read_database_master(database_data):
    result = database_data
    assert result.iloc[0, 15] == "0110LFC10CL010"

def test_read_instrument_master(instrument_data):
    result = instrument_data
    assert result.iloc[0, 10] == "0110LFC10CL010"

def test_lines_instrument_master(instrument_data):
    assert len(instrument_data) == 7
