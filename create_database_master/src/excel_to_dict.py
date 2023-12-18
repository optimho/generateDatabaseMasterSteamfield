import pandas as pd


def excel_to_dict(file_path: str) -> dict:
    """
    This function is to convert a KKS system list in an Excel worksheet into a dictionary

    :param file_path:
    :param kks_systems_df: dataframe of the KKS systems
    :return: dictionary of the instrument master list
    """
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    # This is the dictionary that will be returned
    keys = df['sys']
    values = df['description']
    kks_systems_dict = dict(zip(keys, values))
    return kks_systems_dict



    # # Iterate through the dataframe and add each row to the dictionary
    # for index, row in kks_systems_df.iterrows():
    #     kks_systems_dict[row['KKS']] = row['System']

    return kks_systems_dict