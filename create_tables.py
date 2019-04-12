#!/usr/bin/env python3

import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """This function connects to default database, drops sparkify database
    if already exists and creates sparkify database. Returns a cur and
    conn object.
    """

    # connect to default database
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute(
        "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """This function iterates through drop_table_queries and executes drop
    table queries to drop each table.

    Arguments:
            cur {object} -- Cursor
            conn {object} -- Connection
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """This function iterates through create_table_queries and executes
    create table quesries to create each table.

    Arguments:
            cur {object} -- Cursor
            conn {object} -- Connection
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """This function creates cur and conn objects by calling
    create_database function, then calls both drop_tables and
    create_tables function while passing cur and conn through
    as arguments.
    """

    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
