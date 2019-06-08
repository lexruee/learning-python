#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sqlite3
import logging

logger = logging.getLogger(__name__)
DBFILE = 'movies.sqlite3'

class MovieDBCreator:
    """ Helper class to create the movie databse. """

    MOVIES = [
        (2000, 'Gladiator'),
        (1999, 'Matrix'),
        (2010, 'Inception'),
        (2014, 'Interstellar'),
    ]

    def __init__(self, dbfile):
        self._dbfile = dbfile

        if not self.dbfile_exists():
            self.create_dbfile()

        self._conn = sqlite3.connect(self._dbfile)
        self._cursor = self._conn.cursor()

    def dbfile_exists(self):
        """ Checks if the file exists. """

        return os.path.isfile(self._dbfile)

    def create_dbfile(self):
        """ Creates the file with the given filename. """

        with open(self._dbfile, 'w+'):
            pass

    def create_table(self):
        """ Creates the movie table. """

        logger.info('Create movie table.')
        sql = """
            CREATE TABLE IF NOT EXISTS movies 
            (id INTEGER PRIMARY KEY, year INTEGER, title TEXT)
            """
        self._cursor.execute(sql)

    def insert_movies(self, movies):
        """ Inserts the movie data into the movies table. """

        logger.info('Insert movies into the movie table.')
        for movie in movies:
            self._cursor.execute('INSERT INTO movies (year, title) VALUES (?, ?)', movie)

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
    creator = MovieDBCreator(DBFILE)
    creator.setup()


