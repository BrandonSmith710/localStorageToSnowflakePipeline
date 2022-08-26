###Installation Instructions

The only step here is to make sure the snowflake-python connector is properly installed,
which can be done by issuing the following command through your terminal: 

pip install --upgrade snowflake-connector-python


###Usage Instructions
Once inside the snowflake_project directory, issue the command:

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
Depending upon the file sizes, this could take anywhere from a few seconds to a few minutes.

Once the program has finished, a status message will be printed to your terminal.