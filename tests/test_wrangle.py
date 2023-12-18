import pytest
import create_database_master.src.excel_io_dataframe as xl
import create_database_master.src.wrangle_database_master as wr
import create_database_master.src.excel_to_dict as ed

@pytest.fixture
def kks_systems():
    file_path = '../data/KKS_Systems.xlsx'
    kks_systems_df = xl.read_workbook(file_path, -1, 0)
    return kks_systems_df
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
    wr.wrangle_database_list(instrument_dat, database_dat, version='test')

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

def test_lines_kks_systems(kks_systems):
    #assert type(kks_systems) == dict
    print(ed.excel_to_dict(kks_systems))


def test_excel_to_dict():
    file_path = '../data/KKS_Systems.xlsx'
    test_dict = ed.excel_to_dict(file_path)
    assert type(test_dict) == dict
    assert len(test_dict) == 156
    assert test_dict['ADB'] == 'Grid - 220 kV ODS'
    assert test_dict['BAW'] == 'Earthing & Lightning Protect Sys'
    assert test_dict['UZM'] == 'Protective Strct from Ext Impact'
