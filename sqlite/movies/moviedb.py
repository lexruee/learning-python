#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sqlite3
import logging

logger = logging.getLogger(__name__)
DBFILE = 'movies.sqlite3'

class MovieRepository:
    """ Helper class to query the movie databse. """

    def __init__(self, connection):
        self._conn = connection
   
    def get_movies(self):
        """ Returns a list of movies. """

        cursor = self._conn.cursor()
        cursor.execute('SELECT year, title FROM movies ORDER BY year')
        movies = cursor.fetchall()
        cursor.close()
        return movies


if __name__ == '__main__':
    connection = sqlite3.connect(DBFILE)
    repository = MovieRepository(connection)

    for year, title in repository.get_movies():
        print(f'Year: {year}, Title: {title}')

