#!usr/bin/env python
# -*- coding: utf-8 -*-

'''
Docstring
**********
Title: Create a SQLite3 database and table
Author: Adeel Ahmad
Email: adeelahmad84@me.com

'''

__version__ = "0.1"

import unittest
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, quantity INT)
                """)

# close the database connection
conn.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )