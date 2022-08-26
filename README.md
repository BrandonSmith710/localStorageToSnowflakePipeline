This program allows a user to specify a local directory containing csv files which can be inserted into an existing Snowflake database.
The csv file column headers do not need to be in the same order as the Snowflake table's columns.

###Installation Instructions

The only installation requirements are to have snowflake-python connector and pandas installed,
which can be done by issuing the following commands to your pip installer: 

pip install --upgrade snowflake-connector-python
pip install pandas


###Usage Instructions
Once inside the root directory in your terminal, issue the command:

python app.py

Then, the terminal will prompt you for five bits of information,

1) The Snowflake username, type or paste in your username, then press enter.

2) The Snowflake password, type or paste in your password, then press enter.

3) The Snowflake account, this can be found when logged into Snowflake, by traveling to: Admin > Accounts. Then under the Account field a string consisting of uppercase letters and numbers should be visible, hover the mouse to the right of this string and a copy icon resembling a paperclip should appear. Hover the mouse over this icon and a URL will appear. The portion starting after 'https://' and ending before '.snowflakecomputing.com' is your account name. Type or paste the account name into your terminal, and then press enter.

4) The filepath to the folder containing csv files to insert into the database. Go to this folder in your file manager, and at the top,
click in the filepath box to reveal the path. Enter or paste the exact path into your terminal, and then press enter.

5) The fully qualified table name. This must consist of: warehouse_name.database_name.schema_name.table_name
Type or paste in the fully qualified table name and the press enter.

6) Finally the program will parse through the csv files contained in the folder path, inserting them into the table specified.

Once the program has finished, a status message will be printed to your terminal.
