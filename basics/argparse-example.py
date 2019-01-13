#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexander Rüedlinger'
__license__ = 'MIT'

import argparse
import sys


if __name__ == '__main__':
    description = 'Simple CLI tool'
    version = '0.1'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', action='version', 
            version='%(prog)s {}'.format(version), 
            help='Print version number.')
    parser.add_argument('-u', '--url', dest='url', 
            help='Set URL address.', default='http://localhost:8485')
    parser.add_argument('-s', '--start-time', dest='start_time', type=int,
            help='Set start time.', default=0)
    parser.add_argument('-e', '--end-time', dest='end_time', type=int,
            help='Set end time.', default=10000)
    parser.add_argument('-o', '--output', dest='output', 
            help='Output file.', default='out.txt')
  
    args = parser.parse_args()
