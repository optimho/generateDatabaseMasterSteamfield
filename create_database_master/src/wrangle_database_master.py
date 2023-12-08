"""
Compares the master instrument dataframe and creates a database master dataframe
This is used to create an Excel spreadsheet to import into an access database
for contact energys' device database.

"""

import numpy as np
import pandas as pd
from create_database_master.src import wrangle_configuration as connect


def wrangle_database_list(master_list: pd, database_list: pd, version: str):
    #Takes the new instrument lists, checks the exsisting database lists
    #compiles a new lists with data from both lists and presents the data in a format that
    #can easily be used to import into the new instrument database

    master_instrument_list = master_list
    master_database_list = database_list


    for instrument_list_index in range(master_instrument_list.shape[0]):
        device_is_listed=False
        for database_list_index in range(master_database_list.shape[0]):

            #Check the kks numbers in both lists -- check what indexes should be set 0 is default  #####
            ####  TODO _ NOTE {This is an essential part - compares a unique cell in both workbooks }##################
            ####  TODO _ NOTE {The number at the end indictes the column                            }##################
            ####  TODO _ NOTE {of the cells in the Dataframe to compare                             }##################


            kks_number_instrument_list = master_instrument_list.iloc[instrument_list_index, 10]
            kks_number_database_list = master_database_list.iloc[database_list_index, 15]

            #If you find an instrument that is listed in both lists update the database lists
            #with as much data from the new instrument lists
            if kks_number_instrument_list==kks_number_database_list:
                device_is_listed = True

            ######## WRANGLE DATA HERE ###########  TODO      ###########################################
            #
                # Station Name
                connect.station_name(master_database_list, database_list_index,
                                     name="Tauhara B Steamfield")

                # System
                connect.system_name(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index)

                # Tag
                connect.tag(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index)

                # Point name
                connect.point_name(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index)

                # Function
                connect.function(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index)

                # Type
                master_database_list.iat[database_list_index, 5] = \
                    master_instrument_list.iloc[instrument_list_index, 34]

                # criticality = ? not yet implemented
                connect.criticality(master_database_list, database_list_index, master_instrument_list,
                                 instrument_list_index, val="")

                # Resource Consent = ? not yet implemented
                connect.resource_consent(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index, val="")

                #PCPR = ? not yet implemented
                connect.pcpr(master_database_list, database_list_index, master_instrument_list,
                                         instrument_list_index, val="")

                #KPI = ? not implemented yet
                connect.kpi(master_database_list, database_list_index, master_instrument_list,
                                         instrument_list_index, val="")

                #Nominal operating value
                connect.nominal_operating_value(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index)

                #setting range
                connect.setting_range(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index)

                #Device range
                connect.device_range(master_database_list, database_list_index, master_instrument_list,
                                      instrument_list_index)

                #Device Type TODO: this needs work
                connect.device_type(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)




                # date of entry
                master_database_list.iat[database_list_index, 48] = \
                    ('8/12/2023')

                #master_database_list.iat[database_list_index, 49] = master_instrument_list.iat[instrument_list_index, 1]

                #
                # ######################################################################################################
                # # TODO update the updated record
                # #master_database_list = master_database_list._append(temp_database, ignore_index=True)



            #Chpytesteck if the device was not on the lists of items in the database, then add it
            if (device_is_listed==False) and (master_database_list.shape[0] == database_list_index+1) :

                #copy the last record in the master_database dataframe and append the record to the master database /
                # dataframe
                temp_database: np = master_database_list.loc[master_database_list.shape[0]-1]
                temp_master: np = master_instrument_list.loc[instrument_list_index]

                ###### TODO WRANGLE DATA HERE ##########################################################################
                # a = master_database_list.iat[database_list_index, 0]
                # master_database_list.iat[database_list_index,0] = master_instrument_list.iat[instrument_list_index,1]
                # b = master_database_list.iat[database_list_index, 0]

                master_database_list.iat[database_list_index, 0] = master_instrument_list.iat[instrument_list_index, 1]


                ########################################################################################################
                # append the updated record
                master_database_list = master_database_list._append(temp_database, ignore_index=True)


                #print(f'ADD This to Database List --{instrument_list_index} Updates')
                device_is_listed = True
                ##TODO add master lists item to the the database lists



    return master_database_list
