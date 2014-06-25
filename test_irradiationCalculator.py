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

import unittest
from grsonne import IrradiationCalculator


class TestIrradiationCalculator(unittest.TestCase):
    RESULT_ALLOWANCE = 0.0001

    def setUp(self):
        self.runner = IrradiationCalculator()

    def test_calculate(self):
        self._run_calculation_test(740020, 184970, 0, 0, 1384)
        self._run_calculation_test(740020, 184970, 0, 5, 1312)
        self._run_calculation_test(740020, 184970, 0, 9, 1254)
        self._run_calculation_test(740020, 184970, 0, 10, 1240)
        self._run_calculation_test(740020, 184970, 155, 0, 1384)
        self._run_calculation_test(740020, 184970, 155, 5, 1436)
        self._run_calculation_test(740020, 184970, 180, 25, 1610)
        self._run_calculation_test(740020, 184970, 180, 40, 1630)
        self._run_calculation_test(740020, 184970, 359, 0, 1384)
        self._run_calculation_test(740020, 184970, 359, 55, 562)
        self._run_calculation_test(740020, 184970, 359, 80, 344)
        self._run_calculation_test(740020, 184970, 360, 90, 301)

    def _run_calculation_test(self, x, y, azimut, angle, expected_result):
        self.assertEqual(
            self.runner.calculate(x, y, azimut, angle),
            expected_result)

if __name__ == '__main__':
    unittest.main()