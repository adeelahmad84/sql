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

with sqlite3.connect("new.db") as connection:
        c = connection.cursor()

	# insert multiple records using a tuple
	cities = [
		('Boston', 'MA', 600000),
		('Chicago', 'IL', 2700000),
		('Houston', 'TX', 2100000),
		('Phoenix', 'AZ', 1500000)
		]

	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )