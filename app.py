from module_1 import functions

'''
Collects Snowflake login and account information, folder path information,
and a fully qualified Snowflake table from the user, connects to the user account,
and inserts the contents of the specified folder into the Snowflake table.
'''

if __name__ == '__main__':
    username = input('Enter Snowflake username: ')
    password = input('Enter Snowflake password: ')
    account = input('Enter Snowflake account: ')
    folder_path = input('Enter the filepath for the folder containing csv files for upload: ')
    qualified_table = input('Enter the qualified table name you would like to store the files in: ')
    csv_path_list = functions.get_csv_list(folder_path)
    ctx = functions.get_conn(
	username = username,
	password = password,
	account = account
	)
    functions.load_csvs_to_snowflake_table(
        ctx = ctx,
        qualified_table = qualified_table,
        csv_path_list = csv_path_list
        )
    print('File upload complete')
