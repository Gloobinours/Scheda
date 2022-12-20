import psycopg2
import yaml
import os

def connect():
    """Connect to Postgres via db.yml

    Returns:
        _type_: Connection
    """
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])

def exec_sql_file(path):
    """Execute an sql file

    Args:
        path (string): the path to the sql file
    """
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

def exec_get_all(sql, args={}):
    """Execute and get values from SQL command

    Args:
        sql (string): SQL command
        args (dict, optional): Additional arguments. Defaults to {}.

    Returns:
        list of tuples: Values from the executed SQL command
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall

    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    """Run SQL and do a commit operation

    Args:
        sql (string): SQL command
        args (dict, optional): Additional arguments. Defaults to {}.

    Returns:
        _type_: result from SQL command (if any)
    """
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result