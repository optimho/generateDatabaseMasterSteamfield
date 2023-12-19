"""
    modify signals from the master data worksheet(dataframe).

            #~~Master Database fields
            #0 Stations Name
            #1 System
            #2 Tag
            #3 point
            #4 FUNCTION
            #5 Type of device
            #6 criticallity
            #7 Resource concent
            #8 PECRP yes/no
            #9 KPI (maybe use for SIS) or none
            #10 Nominal operating value
            #11 Setting Range
            #12 Device Range
            #13 Device Type
            #14 Proof (not sure what this is)
            #15 PlantCode (kks number)
            #16 Data
            #17 Store Number
            #18 Drawing number
            #19 note to tester
            #     line 1
            #     line 2
            #     line 3
            #     line 4
            #     line 5
            #     line 6
            #20 Measure Units bar, temperature
            #21 Ideal output
            #22 Measured variable 1
            #23 Measured variable 2
            #24 Measured variable 3
            #25 Measured variable 4
            #26 Measured variable 5
            #27 Measured variable 6
            #28 Measured variable 7
            #29 Ideal output 1
            #30 Ideal output 2
            #31 Ideal output 3
            #32 Ideal output 4
            #33 Ideal output 5
            #34 Ideal output 6
            #35 Ideal output 7
            #36 Digital out 1
            #37 Digital out 2
            #38 Digital out 3
            #39 Digital out 4
            #40 Digital out 5
            #41 Digital out 6
            #42 DigiAliase 1
            #43 DigiAliase 2
            #44 DigiAliase 3
            #45 DigiAliase 4
            #46 DigiAliase 5
            #47 DigiAliase 6
            #48 DateChecked
            #49 Checked By

"""
import datetime as dt

def station_name(master_database_list, database_list_index, name):
    """
    #0 Station Name = name
    :param master_database_list:
    :param database_list_index:
    :param name: the name of the station
    :return:  master_database_list with the station name set
    """
    master_database_list.iat[database_list_index, 0] = name
    return master_database_list


def system_name(master_database_list, database_list_index):
    """
    #1 System = System
    :param kks_systems: a dictionary of kks systems descriptions (ADA, ADB, .. ect)
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database_list with the system name set from the master instrument list
    """

    # kks_code = master_instrument_list.iloc[instrument_list_index, 3][1:]
    # master_database_list.iat[database_list_index, 1] = \
    #     str(master_instrument_list.iloc[instrument_list_index, 15]) + ' ' + \
    #     kks_systems[kks_code]

    return master_database_list


def tag(master_database_list, database_list_index):
    """

    #2 Tag = #4 System +#5 ISA ID +#7 EQ
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database with its tag configured
    """
    # master_database_list.iat[database_list_index, 2] = \
    #     str(master_instrument_list.iloc[instrument_list_index, 4]) + \
    #     master_instrument_list.iloc[instrument_list_index, 5] + \
    #     str(master_instrument_list.iloc[instrument_list_index, 7])

    return master_database_list


def point_name(master_database_list, database_list_index):
    """
    #3 Point name =#15 Equipment
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database_list
    """

    # master_database_list.iat[database_list_index, 3] = \
    #     str(master_instrument_list.iloc[instrument_list_index, 15]) + " " + \
    #     str(master_instrument_list.iloc[instrument_list_index, 16])

    return master_database_list


def function(master_database_list, database_list_index):
    """
    #4 Function = #16 Parameter
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return:
    """
    pass
    # master_database_list.iat[database_list_index, 4] = \
    #     master_instrument_list.iloc[instrument_list_index, 16]

    return master_database_list


def device_model(master_database_list, database_list_index):
    """

    #5 Type = #38 Model of Device
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database_list with type of device set
    """

    # master_database_list.iat[database_list_index, 5] = \
    #     master_instrument_list.iloc[instrument_list_index, 38]

    return master_database_list


def criticality(master_database_list, database_list_index):
    """
    #6 criticality = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: A or B or C depending on the criticality
    :return: master database list
    TODO Implement criticality calculation
    """

    # master_database_list.iat[database_list_index, 6] = \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def resource_consent(master_database_list, database_list_index):
    """
    #7 resource concent = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: yes/no depending on whether it is resource consent or not
    :return: master database list
    TODO Implement criticality calculation
    """

    # master_database_list.iat[database_list_index, 7] = \
    # master_instrument_list.iloc[instrument_list_index,?]

    return master_database_list


def pcpr(master_database_list, database_list_index):
    """
    Could be used for SIS
    #8 PCPR = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: = Yes/No depending on the criticality
    :return: master database list
    """

    master_database_list.iat[database_list_index, 8] = 'NO'
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def kpi(master_database_list, database_list_index):
    """
    #9 kpi = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: = Yes/No
    :return: master database list
    TODO Implement criticality calculation
    """
    pass
    master_database_list.iat[database_list_index, 9] = 'NO'

    return master_database_list


def nominal_operating_value(master_database_list, database_list_index):
    """
    #10 Nominal operating value = #29 operating value
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the nominal operating point set
    """

    # master_database_list.iat[database_list_index, 10] = \
    #     master_instrument_list.iloc[instrument_list_index, 29]

    return master_database_list


def setting_range(master_database_list, database_list_index):
    """
    #11 Nominal operating value = #23 operating value
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the nominal operating point set
    """

    # master_database_list.iat[database_list_index, 11] = \
    #     master_instrument_list.iloc[instrument_list_index, 30]

    return master_database_list


def device_range(master_database_list, database_list_index):
    """
    #12 device range = #28 Instrument range
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set
    """

    # master_database_list.iat[database_list_index, 12] = \
    #     master_instrument_list.iloc[instrument_list_index, 28]

    return master_database_list


def device_type(master_database_list, database_list_index):
    """
    #13 device type = use what was filled in
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set

    """

    # master_database_list.iat[database_list_index, 13] = \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def device_proof(master_database_list, database_list_index):
    """
    #14 device accuracy = depends on #31 parameter
    proof is an accuracy eg value +/- 1%
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set
    TODO need to fix this device type is a number to a table that has a list of devices
    """

    # master_instrument_list.iloc[instrument_list_index, 31] = '+/- 2.5%'

    return master_database_list


def plant_code(master_database_list, database_list_index):
    """
    #15 plant code =
    This fuction does nothing and is here for a future feature
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database, with no changes

    """
    pass
    # master_database_list.iat[database_list_index, 13] = \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def data(master_database_list, database_list_index):
    """
    #16 data = #32 datasheet
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with datasheet
    """

    # master_database_list.iat[database_list_index, 16] = \
    #     master_instrument_list.iloc[instrument_list_index, 32]

    return master_database_list


def order(master_database_list, database_list_index):
    """
    #17 store number = #39 purchase order number
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with drawing number set
    """

    # master_database_list.iat[database_list_index, 17] = \
    #     'PO# ' + str(master_instrument_list.iloc[instrument_list_index, 39])

    return master_database_list


def drawg(master_database_list, database_list_index):
    """
    #18 drawing # = #33 pid drawing
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with drawing number set
    """

    # master_database_list.iat[database_list_index, 18] = \
    #     master_instrument_list.iloc[instrument_list_index, 33]

    return master_database_list


def notes(master_database_list, database_list_index):
    """
    #19 notes to tester = 'rev:' + #35 /n
                          'make:' + #37 /n
                          'install:' + #34 /n
                          'drwg:' + #31 /n


    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return:
    """

    # master_database_list.iat[database_list_index, 19] = 'rev: ' + \
    #                                                     str(master_instrument_list.iloc[
    #                                                             instrument_list_index, 35]) + ' \nmake: ' + \
    #                                                     str(master_instrument_list.iloc[
    #                                                             instrument_list_index, 37]) + ' \ninstall: ' + \
    #                                                     str(master_instrument_list.iloc[
    #                                                             instrument_list_index, 34]) + ' \ndrwg: ' + \
    #                                                     str(master_instrument_list.iloc[instrument_list_index, 31])
    #
    return master_database_list


def date(master_database_list, database_list_index):
    """
    #48 date
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with date set
    """

    master_database_list.iat[database_list_index, 48] = dt.date.today()

    return master_database_list


def who(master_database_list, database_list_index, val):
    """
    #49 who updated
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with whom upated
    """

    master_database_list.iat[database_list_index, 49] = val

    return master_database_list
