import os
from .db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_data.sql')

def list_examples():
    #! This is an example. Remove from your code after test is done
    return exec_get_all('SELECT id, foo FROM example_table')