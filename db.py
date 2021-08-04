import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_users(conn, users):
    sql = ''' INSERT INTO users(username)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, users)
    conn.commit()


def initiate_db():
    database = r"./owasp-top10.db"

    sql_drop_table_user = """ DROP TABLE IF EXISTS users;
    """

    sql_create_table_user = """CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL
                            );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_drop_table_user)
        create_table(conn, sql_create_table_user)
        students = ['James', 'Alex', 'Bill',
                    'Catherine', 'Andy', 'Molly', 'Rose']
        for i in students:
            user = (i,)
            user_id = create_users(conn, user)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    initiate_db()
