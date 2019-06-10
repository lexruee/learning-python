#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import sqlite3
import logging
import json

logger = logging.getLogger(__name__)
DBFILE = 'sensor_data.sqlite3'


def create_table(conn, cursor):
    """ Creates the table. """

    logger.info('Create table.')
    sql = """
        CREATE TABLE IF NOT EXISTS sensor_data (id INTEGER PRIMARY KEY, node TEXT, data TEXT, timestamp DOUBLE, 
        temperature FLOAT, humidity FLOAT, pressure FLOAT)
    """
    cursor.execute(sql)
    conn.commit()

def insert_data(conn, cursor, data):
    """ Inserts the data into the table. """

    logger.info('Insert data into the table.')
    for row in data:
        node = row['node']
        json_data = json.dumps(node)
        temperature, humidity, pressure = row.get('temperature', None), row.get('humidity', None), row.get('pressure', None)
        timestamp = row['timestamp']
        cursor.execute('INSERT INTO sensor_data (node, data, timestamp, temperature, humidity, pressure) VALUES (?, ?, ?, ?, ?, ?)',
                       (node, json_data, timestamp, temperature, humidity, pressure))
        conn.commit()

def read_json_file(json_file):
    """ Reads the contents of a JSON file and returns a Python object. """
    with open(json_file, 'r+') as file:
        json_data = file.readlines()
        return [json.loads(json_object) for json_object in json_data]


if __name__ == '__main__':

    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        data = read_json_file(json_file)

        conn = sqlite3.connect(DBFILE)
        cursor = conn.cursor()

        create_table(conn, cursor)
        insert_data(conn, cursor, data)

        cursor.close()
        conn.close()
    else:
        print('Usage: createdb.py JSON_FILE')

