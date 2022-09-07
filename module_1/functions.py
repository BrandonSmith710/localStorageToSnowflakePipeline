import os
import pandas as pd
import snowflake.connector


def get_conn(username, password, account):
    '''
    Create a connection to snowflake.
    Parameters: username - str; Active snowflake username.
                password - str; Snowflake password associated with username.
                account - str; Snoflake account associated with username.
    Returns: An active Snowflake connection.
    '''

    return snowflake.connector.connect(
        user = username,
        password = password,
        account = account
        )

def get_csv_list(folder_path):
    '''
    Generate a list of file paths for all files in folder_path.
    Parameters: folder_path - str; Path to folder containing csv file(s).
    Returns: List of string paths to files found in folder_path.
    '''

    csv_path_list = []
    for directory, subdir, files in os.walk(folder_path):
        for file in files:
    	    csv_path_list.append(os.path.join(folder_path, file))
    return csv_path_list


def load_csvs_to_snowflake_table(ctx, qualified_table, csv_path_list):
    '''
    Insert the contents of a list of csv files into a qualified snowflake table.
    Parameters: ctx - snowflake.connector.connection.SnowflakeConnection
	        qualified_table - Existing Snowflake table.
	        csv_path_list - list; List containing string paths of csv files.
    '''

    warehouse, db, schema, table = qualified_table.split('.')
    cs = ctx.cursor()
    cs.execute('USE WAREHOUSE {};'.format(warehouse))
    cs.execute('USE DATABASE {};'.format(db))
    cs.execute('USE SCHEMA {};'.format(schema))
    k = []
    i = 0
    for col in cs.describe('SELECT * FROM {};'.format(table)):
        k.append(col[0])
    for csv_file in csv_path_list:
        df = pd.read_csv(csv_file, na_values = 'None')
	if list(df.columns) != k:
            df = pd.DataFrame({col: df[col] for col in k})
        tmp = '{}.csv'.format(i)
        df.to_csv(tmp, index = False)
        cs.execute('PUT file://{}* @%{};'.format(tmp, table))
        cs.execute("COPY INTO {} file_format = (type = csv field_delimiter = ',' skip_header = 1)".format(table))
        i += 1
    cs.close()
    ctx.close()
