"""
Compares the master instrument dataframe and creates a database master dataframe
This is used to create an Excel spreadsheet to import into an access database
for Contact Energy's device database.
"""
import logging

import numpy as np
import pandas as pd
from create_database_master.src import wrangle_functions as connect
from create_database_master.src import modify_functions as mod

def wrangle_database_list(master_list: pd, database_list: pd, kks_systems: dict, version: str):
    # Takes the new instrument lists, checks the exsisting database lists
    # compiles a new lists with data from both lists and presents the data in a format that
    # can easily be used to import into the new instrument database

    master_instrument_list = master_list
    master_database_list = database_list

    for instrument_list_index in range(master_instrument_list.shape[0]):
        device_is_listed = False
        for database_list_index in range(master_database_list.shape[0]):

            # Check the kks numbers in both lists -- check what indexes should be set 0 is default  #####
            ####  TODO _ NOTE {This is an essential part - compares a unique cell in both workbooks }##################
            ####  TODO _ NOTE {The number at the end indictes the column                            }##################
            ####  TODO _ NOTE {of the cells in the Dataframe to compare                             }##################

            kks_number_instrument_list = master_instrument_list.iloc[instrument_list_index, 10]
            kks_number_database_list = master_database_list.iloc[database_list_index, 15]

            # If you find an instrument that is listed in both lists update the database lists
            # with as much data from the new instrument lists
            if kks_number_instrument_list == kks_number_database_list:
                device_is_listed = True

                ######## WRANGLE DATA HERE ###########  TODO      ###########################################
                #
                # 0 Station Name
                connect.station_name(master_database_list, database_list_index,
                                     name="Tauhara B Steamfield")

                # 1 System
                connect.system_name(master_database_list, database_list_index, master_instrument_list, kks_systems,
                                    instrument_list_index)

                # 2 Tag
                connect.tag(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index)

                # 3 Point name
                connect.point_name(master_database_list, database_list_index, master_instrument_list,
                                   instrument_list_index)

                # 4 Function
                connect.funct(master_database_list, database_list_index, master_instrument_list,
                                 instrument_list_index)

                # 5 Type
                connect.device_model(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)

                # 6 criticality = ? not yet implemented
                connect.criticality(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index, val="")

                # 7 Resource Consent = ? not yet implemented
                connect.resource_consent(master_database_list, database_list_index, master_instrument_list,
                                         instrument_list_index, val="")

                # 8 PCPR = ? not yet implemented
                connect.pcpr(master_database_list, database_list_index, master_instrument_list,
                             instrument_list_index, val="")

                # 9 KPI = ? not implemented yet
                connect.kpi(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index, val="")

                # 10 Nominal operating value
                connect.nominal_operating_value(master_database_list, database_list_index, master_instrument_list,
                                                instrument_list_index)

                # 11 setting range
                connect.setting_range(master_database_list, database_list_index, master_instrument_list,
                                      instrument_list_index)

                # 12 Device range
                connect.device_range(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)

                # 13 Device Type TODO: this needs work
                connect.device_type(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index)

                # 14 Device proof TODO: this needs work
                connect.device_proof(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)

                # 15 plant code (KKS):
                connect.plant_code(master_database_list, database_list_index, master_instrument_list,
                                   instrument_list_index)

                # 16 data:
                connect.data(master_database_list, database_list_index, master_instrument_list,
                             instrument_list_index)

                # 17 store number:
                connect.order(master_database_list, database_list_index, master_instrument_list,
                              instrument_list_index)

                # 18 drawin number:
                connect.drawg(master_database_list, database_list_index, master_instrument_list,
                              instrument_list_index)
                # 19 test notes:
                connect.notes(master_database_list, database_list_index, master_instrument_list,
                              instrument_list_index)
                # 48 date of update:
                connect.date(master_database_list, database_list_index, master_instrument_list,
                             instrument_list_index)

                # 48 updater:
                connect.who(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index, 'RF & MduP')

                # master_database_list.iat[database_list_index, 49] = master_instrument_list.iat[instrument_list_index, 1]

                #
                # ######################################################################################################
                # # TODO update the updated record
                # #master_database_list = master_database_list._append(temp_database, ignore_index=True)

            # Chpytesteck if the device was not on the lists of items in the database, then add it
            if (device_is_listed == False) and (master_database_list.shape[0] == database_list_index + 1):
                # copy the last record in the master_database dataframe and append the record to the master database /
                # dataframe
                temp_database: np = master_database_list.loc[master_database_list.shape[0] - 1]
                temp_master: np = master_instrument_list.loc[instrument_list_index]

                ###### TODO WRANGLE DATA HERE ##########################################################################
                # a = master_database_list.iat[database_list_index, 0]
                # master_database_list.iat[database_list_index,0] = master_instrument_list.iat[instrument_list_index,1]
                # b = master_database_list.iat[database_list_index, 0]

                master_database_list.iat[database_list_index, 0] = master_instrument_list.iat[instrument_list_index, 1]

                ########################################################################################################
                # append the updated record
                master_database_list = master_database_list._append(temp_database, ignore_index=True)

                # print(f'ADD This to Database List --{instrument_list_index} Updates')
                device_is_listed = True

                ##Update Master lists item to the the database lists
                # 0 Station Name
                connect.station_name(master_database_list, database_list_index,
                                     name="Tauhara B Steamfield")

                # 1 System
                connect.system_name(master_database_list, database_list_index, master_instrument_list, kks_systems,
                                    instrument_list_index)

                # 2 Tag
                connect.tag(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index)

                # 3 Point name
                connect.point_name(master_database_list, database_list_index, master_instrument_list,
                                   instrument_list_index)

                # 4 Function
                connect.funct(master_database_list, database_list_index, master_instrument_list,
                                 instrument_list_index)

                # 5 Type
                connect.device_model(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)

                # 6 criticality = ? not yet implemented
                connect.criticality(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index, val="")

                # 7 Resource Consent = ? not yet implemented
                connect.resource_consent(master_database_list, database_list_index, master_instrument_list,
                                         instrument_list_index, val="")

                # 8 PCPR = ? not yet implemented
                connect.pcpr(master_database_list, database_list_index, master_instrument_list,
                             instrument_list_index, val="")

                # 9 KPI = ? not implemented yet
                connect.kpi(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index, val="")

                # 10 Nominal operating value
                connect.nominal_operating_value(master_database_list, database_list_index, master_instrument_list,
                                                instrument_list_index)

                # 11 setting range
                connect.setting_range(master_database_list, database_list_index, master_instrument_list,
                                      instrument_list_index)

                # 12 Device range
                connect.device_range(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)

                # 13 Device Type TODO: this needs work
                connect.device_type(master_database_list, database_list_index, master_instrument_list,
                                    instrument_list_index)

                # 14 Device proof TODO: this needs work
                connect.device_proof(master_database_list, database_list_index, master_instrument_list,
                                     instrument_list_index)

                # 15 plant code (KKS):
                connect.plant_code(master_database_list, database_list_index, master_instrument_list,
                                   instrument_list_index)

                # 16 data:
                connect.data(master_database_list, database_list_index, master_instrument_list,
                             instrument_list_index)

                # 17 store number:
                connect.order(master_database_list, database_list_index, master_instrument_list,
                              instrument_list_index)

                # 18 drawin number:
                connect.drawg(master_database_list, database_list_index, master_instrument_list,
                              instrument_list_index)
                # 19 test notes:
                connect.notes(master_database_list, database_list_index, master_instrument_list,
                              instrument_list_index)
                # 48 date of update:
                connect.date(master_database_list, database_list_index, master_instrument_list,
                             instrument_list_index)

                # 48 updater:
                connect.who(master_database_list, database_list_index, master_instrument_list,
                            instrument_list_index, 'RF & MduP')

    return master_database_list

def modify_database_list(master_list: pd, database_list: pd, version: str):
    # Takes the new instrument lists(can be blank for this function), checks the exsisting database lists
    # updates the database master as required
    # can easily be used to import into the new instrument database

    master_instrument_list = master_list
    master_database_list = database_list


    for database_list_index in range(master_database_list.shape[0]):

            # Check the kks numbers in both lists -- check what indexes should be set 0 is default  #####
            ####  TODO _ NOTE {This is an essential part - compares a unique cell in both workbooks }##################
            ####  TODO _ NOTE {The number at the end indictes the column                            }##################
            ####  TODO _ NOTE {of the cells in the Dataframe to compare                             }##################


            ######## WRANGLE DATA HERE ###########  TODO      ###########################################
            #
            # 1 Station Name
            mod.station_name(master_database_list, database_list_index, name="Tauhara B Steamfield")

            # 1 System
            mod.system_name(master_database_list, database_list_index)

            # 2 Tag
            mod.tag(master_database_list, database_list_index)

            # 3 Point name
            mod.point_name(master_database_list, database_list_index)

            # 4 Function
            mod.funct(master_database_list, database_list_index)
            # 5 Type
            mod.device_model(master_database_list, database_list_index)
            # 6 Device range
            mod.device_range(master_database_list, database_list_index)
            # 7 Resource Consent = ? not yet implemented
            mod.resource_consent(master_database_list, database_list_index, val="")
            # 8 PCPR = ? not yet implemented
            mod.pcpr(master_database_list, database_list_index, val="")
            # 9 KPI = ? not implemented yet
            mod.kpi(master_database_list, database_list_index, val="")
            # 10 Nominal operating value
            mod.nominal_operating_value(master_database_list, database_list_index)
            # 11 setting range
            mod.setting_range(master_database_list, database_list_index)
            # 12 Device proof
            mod.device_proof(master_database_list, database_list_index)
            # 35 Device Type
            mod.device_type(master_database_list, database_list_index)
            # 36 test notes:
            mod.procs(master_instrument_list, master_database_list, database_list_index)

            # 37 criticality = ? not yet implemented
            mod.criticality(master_database_list, database_list_index, val="")

            # 38 plant code (KKS):
            mod.plant_code(master_instrument_list, master_database_list, database_list_index)

            # 39 data:
            mod.data(master_database_list, database_list_index)

            # 40 store number:
            mod.order(master_instrument_list, master_database_list, database_list_index)

            # 41 drawin number:
            mod.drawg(master_database_list, database_list_index)

            # 42 checked:
            mod.checked(master_database_list, database_list_index)

            # 43 date of update:
            mod.date(master_database_list, database_list_index)

            # 44 updater:
            mod.who(master_database_list, database_list_index, 'RF & MduP')

            # 45 changed
            mod.changed(master_database_list, database_list_index)

            #46 calculationError
            mod.calculation_error(master_database_list, database_list_index)

    #Add missing columns (run this second last function
    master_database_list = mod.add_missing_columns(master_database_list, database_list_index)

    # reoder the columns in the dataframe
    master_database_list = mod.presenation(master_database_list, database_list_index)
    return master_database_list
