# generate_instrument_database
generate_database_master
This code was built for a specific purpose but could be tweaked for similar use.

The program opens two .xlsx files and matches records in one file to another based on a shared key. It then creates a new .xlsx file based on data in both files.

The program creates a file that can be imported into a company database using data from both files. The company database expects records in a specific format.

With this program, cells can be copied from one workbook to the other or/and manipulated.

The second workbook is in the format expected by the company database. The program will create new records in the second workbook if there is a matching record based on a single column/cell that was specified.

If there is a matching record, that record will be altered in the second workbook using various data manipulation functions, concat, conditional checks and so on.

Included in the project are example .xlxs files with sample data; the code will produce a file called generated_database.xlxs from two files instrument_master_shortList.xlsx, which is a spreadsheet with several industrial instrumentation devices with related information. The database_master_shortList.xlsx is the spreadsheet with the headers and datatypes the database requires.

In this case, there was already some information in the database_master file, and the instrument_master was a newer version so that the resultant file would have the most up to date informtion from the instrument master and some information preserved from the database master.

instrument_master_shortList.xlsx and database_master_shortList.xlsx are copies of database_master and instrument_master and have less records for testing.

The program also has a series of pytest test functions and is an example of creating fixtures and pytests.

Run/execute the generate_database_master.py file to run the program.
