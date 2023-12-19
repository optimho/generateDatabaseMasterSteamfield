import pytest
import create_database_master.src.excel_io_dataframe as xl
import create_database_master.src.wrangle_database_master as wr
import create_database_master.src.excel_to_dict as ed


@pytest.fixture
def database_data():
    #read instrument Database lists|/
    file_path = '../data/database_master_shortList.xlsx'  # Replace this with the path to your workbook 1
    instrument_data_list_df = xl.read_workbook(file_path, -1, 0)
    return instrument_data_list_df

@pytest.fixture
def wrangle_data():
    database_dat = database_data
    wr.modify_database_list(database_dat, version='test')

def test_lines_database_master(database_data):
    assert len(database_data) == 6
def test_read_database_master(database_data):
    result = database_data
    assert result.iloc[0, 15] == "0110LFC10CL010"

def test_output_database_master_system(database_data):
    assert (database_data.iloc[0, 1] + ' ' + database_data.iloc[0, 2]) == 'Wellpad TH11 Common Steam/Water Dump System 10CL010'


# def test_excel_to_dict():
#     file_path = '../data/KKS_Systems.xlsx'
#     test_dict = ed.excel_to_dict(file_path)
#     assert type(test_dict) == dict
#     assert len(test_dict) == 156
#     assert test_dict['ADB'] == 'Grid - 220 kV ODS'
#     assert test_dict['BAW'] == 'Earthing & Lightning Protect Sys'
#     assert test_dict['UZM'] == 'Protective Strct from Ext Impact'
