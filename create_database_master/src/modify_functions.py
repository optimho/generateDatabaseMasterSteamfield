"""
    modify signals from the master data worksheet(dataframe).

            #~~Master Database fields
            #0 Stations Name
            #1 System
            #2 Tag
            #3 point
            #4 Type of device
            #5 Range
            #6 Resource concent
            #7 PECRP yes/no
            #8 KPI (maybe use for SIS) or none
            #9 Setting (like range 0 -1500)
            #10 Nominal operating value (eg 0 - 100%)
            #11 proof
            #12 MVUnit(mm, bar, temp)
            #13 Mvar1(measurement variable 1)
            #14 Mvar2(measurement variable 2)
            #15 Mvar3(measurement variable 3)
            #16 Mvar4(measurement variable 4)
            #17 Mvar5(measurement variable 5)
            #18 Mvar6(measurement variable 6)
            #19 Mvar7(measurement variable 7)
            #20 IdealUnit(mA, mm, bar, temp)
            #21 Ivar1(ideal output 1)
            #22 Ivar2(ideal output 2)
            #23 Ivar3(ideal output 3)
            #24 Ivar4(ideal output 4)
            #25 Ivar5(ideal output 5)
            #26 Ivar6(ideal output 6)
            #27 Ivar7(ideal output 7)
            #28 Dout1(digital out 1)
            #29 Dout2(digital out 2)
            #30 Dout3(digital out 3)
            #31 Dout4(digital out 4)
            #32 Dout5(digital out 5)
            #33 Dout6(digital out 6)
            #34 Device type (This is used as test frequency)
            #36 Procs (notes to tester)
            #37 Plant code
            #38 Data(CCI-DAT-)
            #39 StoresNo
            #40 Drawing No
            #41 Checked
            #42 DateChecked
            #43 checkedBy
            #44 Changed
            #45 calculation error

"""
import datetime as dt
import pandas as pd
from numpy.distutils.fcompiler import str2bool


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
    master_database_list.iat[database_list_index, 1] = master_database_list.iat[database_list_index, 3] + ' ' + \
                                                       master_database_list.iat[database_list_index, 1]

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
    master_database_list.iat[database_list_index, 2] = master_database_list.iat[database_list_index, 2]
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

    master_database_list.iat[database_list_index, 3] = str(master_database_list.iat[database_list_index, 3]) + \
         ' - ' + str(master_database_list.iat[database_list_index, 35]).split()[0]

    #     str(master_instrument_list.iloc[instrument_list_index, 15]) + " " + \
    #     str(master_instrument_list.iloc[instrument_list_index, 16])

    return master_database_list


def funct(master_database_list, database_list_index):
    """
    #4 Funct = #16 Parameter
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return:
    """
    pass
    master_database_list.iat[database_list_index, 4] = master_database_list.iat[database_list_index, 4]
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

    master_database_list.iat[database_list_index, 5] = master_database_list.iat[database_list_index, 5]
    #     master_instrument_list.iloc[instrument_list_index, 38]

    return master_database_list

def device_range(master_database_list, database_list_index):
    """
    #6 device range = #28 Instrument range
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set
    """

    # master_database_list.iat[database_list_index, 12] = \
    #     master_instrument_list.iloc[instrument_list_index, 28]

    return master_database_list


def resource_consent(master_database_list, database_list_index, val):
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

    master_database_list.iat[database_list_index, 7] = 'NO'
    # master_instrument_list.iloc[instrument_list_index,?]

    return master_database_list


def pcpr(master_database_list, database_list_index, val):
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


def kpi(master_database_list, database_list_index, val):
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
    #     master_instrument_list.iloc[instrument_list_index, 23]

    #     master_instrument_list.iloc[instrument_list_index, 30]

    return master_database_list

def device_proof(master_database_list, database_list_index):
    """
    #12 device accuracy = depends on #31 parameter
    proof is an accuracy eg value +/- 1%
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set
    TODO need to fix this device type is a number to a table that has a list of devices
    """

    master_database_list.iat[database_list_index, 12] = "+/- 1.0%"
    return master_database_list

##
##   TODO all the digital inputs and ideal outputs measured vlues and units
##   TDOO Have not been implemented, use what is filled in already
##

def device_type(master_database_list, database_list_index):
    """
    #35 device type = frequency of test (eg 1 year, 2 year, 5 year)
        leave blank for now.
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with the instrument range set

    """

    master_database_list.iat[database_list_index, 35] = ''
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list

def procs(master_instrument_list, master_database_list, database_list_index):
    """
    #36 notes to tester = 'rev:' + #35 /n
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
    #                                                             database_list_index, 35]) + ' \nmake: ' + \
    #                                                     str(master_instrument_list.iloc[
    #                                                             database_list_index, 37]) + ' \ninstall: ' + \
    #                                                     str(master_instrument_list.iloc[
    #                                                             database_list_index, 34]) + ' \ndrwg: ' + \
    #                                                     str(master_instrument_list.iloc[database_list_index, 31])

    master_database_list.iat[database_list_index, 19] = 'rev: ' \
                                                        # + \
                                                        # str(master_instrument_list.iloc[
                                                        #         database_list_index, 35]) + ' \nmake: ' + \
                                                        # str(master_instrument_list.iloc[
                                                        #         database_list_index, 37]) + ' \ninstall: ' + \
                                                        # str(master_instrument_list.iloc[
                                                        #         database_list_index, 34]) + ' \ndrwg: ' + \
                                                        # str(master_instrument_list.iloc[database_list_index, 31])
    return master_database_list
def criticality(master_database_list, database_list_index, val):
    """
    #37 criticality = ? index
    does nothing at present
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :param val: A or B or C depending on the criticality
    :return: master database list
    TODO Implement criticality calculation
    """

    master_database_list.iat[database_list_index, 37] = master_database_list.iat[database_list_index, 37]
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list



def plant_code(master_database_list, database_list_index):
    """
    #38 plant code =
    This fuction does nothing and is here for a future feature
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database, with no changes

    """
    # master_database_list.iat[database_list_index, 38] = \
    #     master_database_list.iat[database_list_index, 38]
    #
    #
    # \
    # master_instrument_list.iloc[instrument_list_index, ]

    return master_database_list


def data(master_database_list, database_list_index):
    """
    #39 data = #32 datasheet
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with datasheet
    """

    # master_database_list.iat[database_list_index, 39] = master_database_list.iat[database_list_index, 39]
    # \
    #     master_instrument_list.iloc[instrument_list_index, 32]

    return master_database_list



def order(master_instrument_list, master_database_list, database_list_index):
    """
    #40 order or stores number index = #39 stores number
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with drawing number set
    """

    # The value you are looking for
    value_to_find = master_database_list.iat[database_list_index, 38]
    result_index = master_instrument_list.index[master_instrument_list['TAG NUMBER'] == value_to_find].tolist()
    print(result_index[0])

    master_database_list.iat[database_list_index, 40] = 'PO# ' + str(master_instrument_list.iloc[result_index[0], 39])


    return master_database_list


def drawg(master_database_list, database_list_index):
    """
    #41 drawing # = #33 pid drawing
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with drawing number set
    """

    # master_database_list.iat[database_list_index, 18] = \
    #     master_instrument_list.iloc[instrument_list_index, 33]

    return master_database_list



def checked(master_database_list, database_list_index):
    """
    #42 checked index
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with date set
    """

    master_database_list.iat[database_list_index, 42] = str2bool("no")

    return master_database_list

def date(master_database_list, database_list_index):
    """
    #43 dateChecked index
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with date set
    """

    master_database_list.iat[database_list_index, 43] = dt.date.today()

    return master_database_list

def who(master_database_list, database_list_index, val):
    """
    #44 who updated the database index
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with whom upated
    """

    master_database_list.iat[database_list_index, 44] = val

    return master_database_list
def changed(master_database_list, database_list_index):
    """
    #45 changed index
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with date set
    """

    master_database_list.iat[database_list_index, 45] = str2bool("no")

    return master_database_list

def calculation_error(master_database_list, database_list_index):
    """
    #45 calculatiion error index
    :param master_database_list:
    :param database_list_index:
    :param master_instrument_list:
    :param instrument_list_index:
    :return: master database list with date set
    """

    master_database_list.iat[database_list_index, 46] = str2bool("yes")

    return master_database_list