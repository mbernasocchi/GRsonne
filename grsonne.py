# coding=utf-8
'''
GRsonne

Contact : marco@opengis.ch

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 3 of the License, or
     (at your option) any later version.

'''

__author__ = 'marco@opengis.ch'
__date__ = '15/06/2014'

import os
import sys
import getopt


class IrradiationCalculator(object):

    def __init__(self, db, host=None, port=None, user=None, password=None):
        self.input_x = None
        self.input_y = None
        self.center_x = None
        self.center_y = None

        self.input_azimut = None
        self.min_azimut = None
        self.max_azimut = None

        self.input_angle = None
        self.min_angle = None
        self.max_angle = None

        self.field_names = []

        self.irradiation = None

        if os.path.isfile(db):
            #use SQLITE
            import sqlite3
            self.db = sqlite3.connect(db)
            self.table_name = 'irradiation'
            self.column_prefix = 'I'
            self.db_value_placeholder = '?'
        else:
            #use PostgreSQL
            import psycopg2
            self.db = psycopg2.connect(database=db, host=host, port=port,
                                       user=user, password=password)
            self.table_name = 'gr_sonne.irradiation'
            self.column_prefix = 'i'
            self.db_value_placeholder = '%s'

    def calculate(self, input_x, input_y, input_azimut, input_angle):
        self.input_x = input_x
        self.input_y = input_y
        self.input_azimut = input_azimut
        self.input_angle = input_angle

        self.check_input()
        self.center_x, self.center_y = self.get_center_coords()
        self._calculate_field_names()
        values = self.get_values()
        print values
        coefficients = self._calculate_coeficients()
        self.irradiation = self._run_calc(values, coefficients)
        print self.irradiation
        return self.irradiation

    @staticmethod
    def _run_calc(values, coefficients):
        min_azimut_max_angle = (values['min_azimut_max_angle']
                                * coefficients['min_azimut_max_angle'])
        max_azimut_max_angle = (values['max_azimut_max_angle']
                                * coefficients['max_azimut_max_angle'])
        min_azimut_min_angle = (values['min_azimut_min_angle']
                                * coefficients['min_azimut_min_angle'])
        max_azimut_min_angle = (values['max_azimut_min_angle']
                                * coefficients['max_azimut_min_angle'])

        return int(round(min_azimut_max_angle + max_azimut_max_angle +
                        min_azimut_min_angle + max_azimut_min_angle, 0))

    def get_values(self):
        values = (self.center_x, self.center_y)
        sql = 'SELECT %s%s, %s%s, %s%s, %s%s ' % (
            self.column_prefix, self.field_names[0],
            self.column_prefix, self.field_names[1],
            self.column_prefix, self.field_names[2],
            self.column_prefix, self.field_names[3])
        sql += 'FROM %s ' % self.table_name
        sql += 'WHERE x = %s AND y = %s' % (self.db_value_placeholder,
                                            self.db_value_placeholder)

        print sql
        print values
        cursor = self.db.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return {'min_azimut_max_angle': int(result[0]),
                'max_azimut_max_angle': int(result[1]),
                'min_azimut_min_angle': int(result[2]),
                'max_azimut_min_angle': int(result[3])}

    def check_input(self):
        check_errors = []

        error_template = 'Invalid %s: Valid range is %s - %s, found %s'

        error_message = error_template % ('x', 693000, 834000, self.input_x)
        if self.input_x < 693000 or self.input_x > 834000:
            check_errors.append(error_message)

        error_message = error_template % ('y', 114700, 215000, self.input_y)
        if self.input_y < 114700 or self.input_y > 215000:
            check_errors.append(error_message)

        error_message = error_template % ('azimut', 0, 360, self.input_azimut)
        if self.input_azimut < 0 or self.input_azimut > 360:
            check_errors.append(error_message)
        if self.input_azimut == 360:
            self.input_azimut = 0

        error_message = error_template % ('angle', 0, 90, self.input_angle)
        if self.input_angle < 0 or self.input_angle > 90:
            check_errors.append(error_message)

        if check_errors:
            raise ValueError(check_errors)

    def get_center_coords(self):
        #change 693000 - 693099 to 693050
        x = int(self.input_x / 100) * 100 + 50

        #change 114700 - 114799 to 114750
        y = int(self.input_y / 100) * 100 + 50

        return x, y

    def _calculate_coeficients(self):
        azimut_step = 0.05
        angle_step = 0.1

        delta_azimut = self.input_azimut - self.min_azimut
        print 'Delta Azimut: %s' % delta_azimut

        delta_angle = self.input_angle - self.min_angle
        print 'Delta Angle: %s' % delta_angle

        #linear inerpolation
        min_azimut_max_angle = ((azimut_step * (20 - delta_azimut)) *
                               (angle_step * delta_angle))

        max_azimut_max_angle = ((azimut_step * delta_azimut) *
                               (angle_step * delta_angle))

        min_azimut_min_angle = ((azimut_step * (20 - delta_azimut)) *
                               (angle_step * (10 - delta_angle)))

        max_azimut_min_angle = ((azimut_step * delta_azimut) *
                               (angle_step * (10 - delta_angle)))


        coefficients_total = (min_azimut_max_angle + max_azimut_max_angle +
                            min_azimut_min_angle + max_azimut_min_angle)

        # check that the coefficients sum up to 1.0
        if abs(coefficients_total - 1) > 0.01:
            error = ('The coefficients don\'t sum up to 1.0, found: %s' %
                     coefficients_total)
            raise ValueError(error)

        return {
            'min_azimut_max_angle': min_azimut_max_angle,
            'max_azimut_max_angle': max_azimut_max_angle,
            'min_azimut_min_angle': min_azimut_min_angle,
            'max_azimut_min_angle': max_azimut_min_angle}

    def _calculate_field_names(self):
        # 7 needs XXX AND 20
        # 234 needs 220 and 240
        # 358 needs 340 and XXX
        min_azimut = (self.input_azimut // 20) * 20

        max_azimut = min_azimut + 20

        # save the numeric version
        self.min_azimut = min_azimut
        self.max_azimut = max_azimut

        if max_azimut == 360:
            max_azimut = 0

        # convert 40 to 040
        min_azimut = str(min_azimut)
        min_azimut = min_azimut.zfill(3)
        max_azimut = str(max_azimut)
        max_azimut = max_azimut.zfill(3)

        # 7 needs 0 AND 10
        # 56 needs 50 and 60
        # 89 needs 80 and 90
        min_angle = (self.input_angle // 10) * 10
        if min_angle == 90:
            min_angle = 80
        max_angle = min_angle + 10

        # save the numeric version
        self.min_angle = min_angle
        self.max_angle = max_angle

        # convert 0 to 00
        min_angle = str(min_angle)
        min_angle = min_angle.zfill(2)
        max_angle = str(max_angle)
        max_angle = max_angle.zfill(2)

        f1 = '%s_%s' % (min_azimut, max_angle)
        f2 = '%s_%s' % (max_azimut, max_angle)

        if min_angle == '00':
            min_azimut = 'xxx'
            max_azimut = 'xxx'
        f3 = '%s_%s' % (min_azimut, min_angle)
        f4 = '%s_%s' % (max_azimut, min_angle)

        # TODO REMOVE HACK when new DB
        if self.db_value_placeholder == '?':
            f1 = f1[:-1]
            f2 = f2[:-1]
            f3 = f3[:-1]
            f4 = f4[:-1]
        # END remove
        self.field_names = (f1, f2, f3, f4)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'ht', ['help', 'test'])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, 'for help use --help'
        return 2

    for o, a in opts:
        if o in ('-h', '--help'):
            print_help()
            return 1

        if o == '--test':
            print 'Running Tests'
            return os.system('python test_irradiationCalculator.py')

    calculator = IrradiationCalculator('/home/marco/Documents/work/QGIS/renewables-now.com/GRsonne/gr_mod.sqlite')
    calculator = IrradiationCalculator('spatial_data')
    if len(args) == 4:
        args = [int(arg) for arg in args]
        calculator.calculate(*args)
        return 0
    else:
        print_help()
        return 1


def print_help():
    print 'Call as following:'
    print 'python grsonne.py x y azimut angle'
    print 'python grsonne.py 740020 184970 346 47'
    print '\nor to run the regresion tests call: python grsonne.py --test'

if __name__ == '__main__':
    sys.exit(main())
