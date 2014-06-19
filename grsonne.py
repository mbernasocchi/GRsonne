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


class IrrdiationCalculator(object):

    def __init__(self, x, y, azimut, angle):
        self.x = x
        self.y = y
        self.center_x = None
        self.center_y = None

        self.azimut = azimut
        self.azimut_fields = ()
        self.angle = angle
        self.angle_fields = ()
        self.field_names = []

        self.irridation = None
        self.check_input()
        self.db = sqlite3.connect(
            '/home/marco/Documents/work/QGIS/renewables-now.com/GRsonne/gr_mod.sqlite')
        self.cursor = self.db.cursor()

    def run(self):
        self.check_input()
        self.center_x, self.center_y = self.get_center_coords()
        self._calculate_field_names()


    def _run_calc(x, y, azimut, angle):
        field = 'I%s_%s' % (azimut, angle/10)
        field = '%s, %s' % (field, field)

        values = (x, y)
        sql = "SELECT %s from 'GRsonne' WHERE x = ? AND y = ?" % field
        print sql
        #_get_db_data(sql, values)


    def _get_db_data(sql, values):
        db = sqlite3.connect(
            '/home/marco/Documents/work/QGIS/renewables-now.com/GRsonne/gr_mod.sqlite')

        c = db.cursor()
        c.execute(sql, values)
        res = c.fetchone()
        print res[0]

    def check_input(self):
        check_errors = []

        error_template = 'Invalid %s: Valid range is %s - %s, found %s'

        error_message = error_template % ('x', 693000, 834000, self.x)
        if self.x < 693000 or self.x > 834000:
            check_errors.append(error_message)

        error_message = error_template % ('y', 114700, 215000, self.y)
        if self.y < 114700 or self.y > 215000:
            check_errors.append(error_message)

        error_message = error_template % ('azimut', 0, 360, self.azimut)
        if self.azimut < 0 or self.azimut > 360:
            check_errors.append(error_message)
        if self.azimut == 360:
            self.azimut = 0

        error_message = error_template % ('angle', 0, 90, self.angle)
        if self.angle < 0 or self.angle > 90:
            check_errors.append(error_message)

        if check_errors:
            raise ValueError(check_errors)

    def get_center_coords(self):
        #change 693000 - 693099 to 693050
        x = int(self.x / 100) * 100 + 50

        #change 114700 - 114799 to 114750
        y = int(self.y / 100) * 100 + 50

        return x, y

    def _calculate_field_names(self):
        # 7 needs XXX AND 20
        # 234 needs 220 and 240
        # 358 needs 340 and XXX
        min_azimut = (self.azimut // 20) * 20

        max_azimut = min_azimut + 20
        if max_azimut == 360:
            max_azimut = 0

        # convert 40 to 040
        min_azimut = str(min_azimut)
        min_azimut = min_azimut.zfill(3)
        max_azimut = str(max_azimut)
        max_azimut = max_azimut.zfill(3)
        self.azimut_fields = (min_azimut, max_azimut)

        # 7 needs 0 AND 10
        # 56 needs 50 and 60
        # 89 needs 80 and 90
        min_angle = (self.angle // 10) * 10
        if min_angle == 90:
            min_angle = 80
        max_angle = min_angle + 10

        # convert 0 to 00
        min_angle = str(min_angle)
        min_angle = min_angle.zfill(2)
        max_angle = str(max_angle)
        max_angle = max_angle.zfill(2)
        self.angle_fields = (min_angle, max_angle)

        f1 = '%s_%s' % (min_azimut, max_angle)
        f2 = '%s_%s' % (max_azimut, max_angle)

        if min_angle == '00':
            min_azimut = 'xxx'
            max_azimut = 'xxx'
        f3 = '%s_%s' % (min_azimut, min_angle)
        f4 = '%s_%s' % (max_azimut, min_angle)

        self.field_names = [f1, f2, f3, f4]


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
            calculator = IrrdiationCalculator(*args)
        else:
            calculator = IrrdiationCalculator(740020, 184970, 181, 45)

        calculator.run()

if __name__ == "__main__":
    sys.exit(main())
