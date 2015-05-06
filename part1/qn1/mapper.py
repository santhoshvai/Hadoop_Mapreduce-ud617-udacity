#!/usr/bin/python

"""
Gives sales breakdown of every product category across all the stores
"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
	date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)
