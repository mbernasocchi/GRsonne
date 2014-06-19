# coding=utf-8
"""
GRsonne

Contact : marco@opengis.ch

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 3 of the License, or
     (at your option) any later version.

"""
__author__ = 'marco@opengis.ch'
__date__ = '15/06/2014'

import sys
import getopt
import sqlite3


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2
    if len(args) == 4:
        args = [int(arg) for arg in args]
        run(*args)
    else:
        run(740020, 184970, 181, 45)


def run(x, y, azimut, angle):
    x, y, azimut, angle = _sanitize_input(x, y, azimut, angle)
    _run_calc(x, y, azimut, angle)


def _run_calc(x, y, azimut, angle):
    field = '%s_%s' % (azimut, angle)
    field = 'xxx_00'

    values = (field, x, y)
    sql = "SELECT ? from 'GRsonne' WHERE x = ? AND y = ?"
    sql = "SELECT %s from 'GRsonne' WHERE x = %s AND y = %s" % values
    print sql
    _get_db_data(sql, values)


def _get_db_data(sql, values):
    c = sqlite3.connect(
        '/home/marco/Documents/work/QGIS/renewables-now.com/GRsonne/gr_mod.sqlite')
    for r in c.execute(sql):
        print r



def _sanitize_input(x, y, azimut, angle):
    sanitize_errors = []

    error_template = 'Invalid %s: Valid range is %s - %s, found %s'

    error_message = error_template % ('x', 693050, 833950, x)
    #change 693000 - 693099 to 693050
    x = int(x / 100) * 100 + 50
    if x < 693050 or x > 833950:
        sanitize_errors.append(error_message)

    error_message = error_template % ('y', 114750, 214950, y)
    #change 114700 - 114799 to 114750
    y = int(y / 100) * 100 + 50
    if y < 114750 or y > 214950:
        sanitize_errors.append(error_message)

    error_message = error_template % ('azimut', 0, 360, azimut)
    azimut = int(round(azimut, -1))
    if azimut < 0 or azimut > 360:
        sanitize_errors.append(error_message)
    if azimut == 360:
        azimut = 0

    error_message = error_template % ('angle', 0, 90, angle)
    angle = int(round(angle, -1))
    if angle < 0 or angle > 90:
        sanitize_errors.append(error_message)

    if sanitize_errors:
        raise ValueError(sanitize_errors)

    return x, y, azimut, angle


if __name__ == "__main__":
    sys.exit(main())
