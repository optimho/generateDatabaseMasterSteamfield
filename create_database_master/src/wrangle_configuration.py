
"""
    connect signals from the master instrument datasheet(dataframe) to the master data frame.

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


            #~~Master Instrument fields ~~~~~~~~~~          ~~~~~~~~Master Database
            #0 - Item number                                      #
            #1 - Plant Short Code                                 #
            #2 - Part of the system                               #
            #3 - System                                           #
            #4 - System                                           #
            #5 - ISA ID (PI or LT or LIT ans so on                #
            #6 - EQ (CP, CL exc)                                  #
            #7 - EQ                                               #
            #8 - com (not used)                                   #
            #9 - item reference                                   #
            #10 Tag number ---                                    #
            #11 equipment - Well TH11                             #
            #12 parameter like Pressure, Level                    #
            #13 line (pipe) or branch number                      #
            #14 LINE SIZE (mm) like 300mm                         #
            #15 line spec (not sure what this is )                #
            #16 service like condensate or LP two phase           #
            #17 minpressure - 0bar or full                        #
            #18 max pressure                                      #
            #19 min temperature                                   #
            #20 max temperature                                   #
            #21 min flow                                          #
            #22 max flow                                          #
            #23 Units like Bar(g)                                 #
            #24 instrument range                                  #
            #25 Operating value                                   #
            #26 calibrated range                                  #
            #27 Instalation drawing                               #
            #28 datasheet                                         #
            #29 P&ID drawing number                               #
            #30 notes about installation                          #
            #31 revision                                          #
            #32 Vendor                                            #
            #33 make                                              #
            #34 model of device                                   #
            #35 PO number                                         #
            #36 recieved date                                     #
            #37 failsafe                                          #
"""
# from nis import match


def station_name(master_database_list, database_list_index, name):
    """
    Station Name = name
    :param master_database_list:
    :param database_list_index:
    :param name: the name of the station
    :return:  master_database_list with the station name set
    """
    master_database_list.iat[database_list_index, 0] = name
    return master_database_list

def system_name(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    System = System
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database_list with the system name set from the master instrument list
    """
    master_database_list.iat[database_list_index, 1] = \
    master_instrument_list.iloc[instrument_list_index, 3]
    return master_database_list


def tag(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    Tag = System + ISA ID + EQ
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database with its tag configured
    """
    master_database_list.iat[database_list_index, 2] = \
    str(master_instrument_list.iloc[instrument_list_index, 4]) + \
    master_instrument_list.iloc[instrument_list_index, 5] + \
    str(master_instrument_list.iloc[instrument_list_index, 7])

    return master_database_list


def point_name(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    Point name = Equipment
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database_list
    """

    master_database_list.iat[database_list_index, 3] = \
    master_instrument_list.iloc[instrument_list_index, 11]

    return master_database_list

def function(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    Function = Parameter
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return:
    """

    master_database_list.iat[database_list_index, 4] = \
    master_instrument_list.iloc[instrument_list_index, 12]

    return master_database_list

def type(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """

    #5 Type = #34 Model of Device
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master_database_list with type of device set
    """

    master_database_list.iat[database_list_index, 5] = \
    master_instrument_list.iloc[instrument_list_index, 34]

    return master_database_list

def criticality(master_database_list, database_list_index, master_instrument_list, instrument_list_index, val):
    """
    # criticality = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: A or B or C depending on the criticality
    :return: master database list
    TODO Implement criticality calculation
    """
    pass
    # master_database_list.iat[database_list_index, 6] = \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def resource_consent(master_database_list, database_list_index, master_instrument_list, instrument_list_index, val):
    """
    # resource concent = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: yes/no depending on whether it is resource consent or not
    :return: master database list
    TODO Implement criticality calculation
    """
    pass
    # master_database_list.iat[database_list_index, 7] = \
    # master_instrument_list.iloc[instrument_list_index,?]

    return master_database_list


def pcpr(master_database_list, database_list_index, master_instrument_list, instrument_list_index, val):
    """
    # PCPR = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: = Yes/No depending on the criticality
    :return: master database list
    TODO Implement criticality calculation
    """
    pass
    # master_database_list.iat[database_list_index, 6] = \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list

def kpi(master_database_list, database_list_index, master_instrument_list, instrument_list_index, val):
    """
    # kpi = ?
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: = Yes/No depending on the criticality
    :return: master database list
    TODO Implement criticality calculation
    """
    pass
    # master_database_list.iat[database_list_index, 6] = \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list

def nominal_operating_value(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    #10 Nominal operating value = #25 operating value
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the nominal operating point set
    """

    master_database_list.iat[database_list_index, 10] = \
    master_instrument_list.iloc[instrument_list_index, 25]

    return master_database_list

def setting_range(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    #11 Nominal operating value = #26 operating value
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the nominal operating point set
    """

    master_database_list.iat[database_list_index, 11] = \
    master_instrument_list.iloc[instrument_list_index, 26]

    return master_database_list

def device_range(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    #12 device range = #24 Instrument range
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set
    """

    master_database_list.iat[database_list_index, 12] = \
    master_instrument_list.iloc[instrument_list_index, 24]

    return master_database_list

def device_type(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
    """
    #13 device range = #34 Instrument range
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set
    TODO need to fix this device type is a number to a table that has a list of devices
    """
    pass
    #master_database_list.iat[database_list_index, 13] = \
    #master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def device_proof(master_database_list, database_list_index, master_instrument_list, instrument_list_index):
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

    # match master_instrument_list.iloc[instrument_list_index,31]:
    #     case '':
    #         master_database_list.iat[database_list_index, 14] = '+/- 2.5%'
    #     case '':
    #         print()



    return master_database_list