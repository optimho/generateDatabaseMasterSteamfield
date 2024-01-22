# generate_instrument_database
generate_database_master by running make_database_master.py script

This code was built for a specific purpose but could be tweaked for similar use.
The use case here is there is two spreadsheets that contains information about installed instrumentation.
One sheet was created by the installation crew (Instrument_Master) and one was created by people collecting 
data for the project hence referred to as the database_master.
the information may have originally come from the installation crew, but might have had a few revisions since.

The one common cell is the KKS number, so the scripts matches the KKS number from both sheets and makes a new worksheet 
from information the is contained in the both of them, the installation crew worksheet is treated as the
master. so if there is useful information put it into the new worksheet.

Another problem was the sequence of the cells that the database requires is slightly different to both these
work sheets, so the most useful use of this script is to arrange the cell order so that it can be copied
and pasted into the Contact Energy device database.

The other half useful thing is that this is a good example of using tests in code and using pandas 
for data manipulation. This script will be on github called generateDataBaseMaster

The program opens two .xlsx files and matches records in one file to another based on a shared Cell. 
It then creates a new .xlsx file called new 'device table.xlsx' based on data in both files.

The program creates a file that can be imported into a company database using data from both files. 
The company database expects records in a specific format.

In this case, there was already some information in the database_master file, and 
the instrument_master was a newer version so that the resultant file would have the most up to date 
information from the instrument master and some information preserved from the database master.

instrument_master_shortList.xlsx and database_master_shortList.xlsx are copies of database_master and 
instrument_master and have less records for testing.

The program also has a series of pytest test functions and is an example of creating fixtures and pytests.

Run/execute the modify_database_master.py file to run the program.
After the file generated_datbase_v5.xlsx is created, it can be imported into the company database
after removing the index column. 

Master sources:
The Instrument master file is TABG-CEL-0-000-CCI-LST-1401_7.8.xlsx
The database master file is Templates Entry Instrument Data (DEC  19) - Revision 2.xlsx
For testing with a reduced number of records, use 'Templates Entry Instrument Data.xlsx'.

The database master file has a small bit of work done to it.
Remove the first row, to do this select the first row and right click and select delete.
Then remove the index column, to do this select the first column cntr 'L' to remove the 
filter and then click header off. then you can delete the first row.

Then save the file as a Templates Entry Instrument Full.xlsx file.
This file is used for converting to a file called generated_database_v6.0.xlsx

generated_database_v6.0.xlsx can be used to copy into the device database.

A few things to check, have you got the same amount of EXCEL rows in the output file as you had in the 
data file, if not then there was some duplication in the data file.

check to see if !@! symbol has not been prefixed to the system name, this is a flag to say that the system has
a duplicated system name as well as a duplicated tag number.
Manually fix these errors.


