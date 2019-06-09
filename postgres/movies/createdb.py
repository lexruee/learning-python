#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import psycopg2
import logging

logger = logging.getLogger(__name__)
DBHOST = 'localhost'
DBNAME = 'movies'
DBUSER = 'postgres'
DBPASSWORD = 'example'


class MovieDBCreator:
    """ Helper class to create the movie databse. """

    MOVIES = [
        (2000, 'Gladiator'),
        (1999, 'Matrix'),
        (2010, 'Inception'),
        (2014, 'Interstellar'),
    ]

    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def create_table(self):
        """ Creates the movie table. """

        logger.info('Create movie table.')
        sql = """
            CREATE TABLE IF NOT EXISTS movies 
            (id SERIAL PRIMARY KEY, year INTEGER, title TEXT)
            """
        self._cursor.execute(sql)

    def insert_movies(self, movies):
        """ Inserts the movie data into the movies table. """

        logger.info('Insert movies into the movie table.')
        for movie in movies:
            self._cursor.execute('INSERT INTO movies (year, title) VALUES (%s, %s)', movie)

    def _cleanup(self):
        """ Closes the cursor and the db connection. """

        logger.info('Close resources.')
        self._cursor.close()
        self._conn.close()

    def setup(self):
        """ Setups the movie database. """

        logger.info('Setup the database.')
        self.create_table()
        self.insert_movies(self.MOVIES)
        self._conn.commit()
        logger.info('Do nothing since the database already exists.')
        self._cleanup()


if __name__ == '__main__':
    conn = psycopg2.connect(host=DBHOST, dbname=DBNAME, user=DBUSER, password=DBPASSWORD)
    creator = MovieDBCreator(conn)
    creator.setup()


