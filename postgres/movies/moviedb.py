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
    connection = psycopg2.connect(host=DBHOST, dbname=DBNAME, user=DBUSER, password=DBPASSWORD)
    repository = MovieRepository(connection)

    for year, title in repository.get_movies():
        print(f'Year: {year}, Title: {title}')

