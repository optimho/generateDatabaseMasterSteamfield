"""
Abbreviate the text in a specific column of the dataframe.
Use the contact energy standard document number 10000002582 revision 2

"""
import pandas as pd
import create_database_master.src.excel_io_dataframe as xl
import logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to replace words
def replace_words(text, replacement_dict, case_sensitive=False):
    words = text.split()
    replaced_words = [replacement_dict.get(word, word) for word in words]
    return ' '.join(replaced_words)

def abbreviate_text(dataframe: pd.DataFrame, column: str = 'System',
                    abbreviation_xl='../../Data/ContactEnergy_abbreviations.xlsx', version:str='') -> pd.DataFrame:
    """
    This function is to abbreviate the text in a specific column of the dataframe.
    :param dataframe: dataframe to be modified
    :param column: column to be modified
    :param abbreviation_xl: a path to an excel work book that contains a list of abbreviations
    :return: dataframe with the modified column
    """

    file_path = abbreviation_xl
    column = column
    abbreviations_df = xl.read_workbook(file_path, -1, 0)

    abbreviation_dict = dict(zip(abbreviations_df['FULL WORD'], abbreviations_df['ABBREVIATION']))
    print(abbreviation_dict)

    for index, row in dataframe.iterrows():
        #print(index, row[column])
        text = row[column]
        row[column] = (replace_words(text.upper(), abbreviation_dict, case_sensitive=True))
        dataframe.at[index, column] = row[column]

    print(dataframe['System'])
    xl.create_excel_from_dataframe(dataframe, f'../Data/abbreviated_data{version}.xlsx')
    return dataframe


if __name__ == '__main__':

    file_path = '../../data/generated_database_v6.0.xlsx'  # Replace this with the path to your workbook
    data_base = xl.read_workbook(file_path, -1, 0)
    abbreviate_text(data_base, 'System', '../../Data/ContactEnergy_abbreviations.xlsx')
