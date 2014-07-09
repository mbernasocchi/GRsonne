# coding=utf-8
"""
GRsonne

Contact : marco@opengis.ch

.. note:: This program is free software: you can redistribute it and/or
modify it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

__author__ = 'marco@opengis.ch'
__date__ = '15/06/2014'

import unittest
from sqlite3 import OperationalError
from psycopg2 import ProgrammingError
from grsonne import IrradiationCalculator


class TestIrradiationCalculator(unittest.TestCase):
    RESULT_ALLOWANCE = 0.0001

    def setUp(self):
        # self.runner = IrradiationCalculator('spatial_data')
        self.runner = IrradiationCalculator('test_fixtures.sqlite')

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

    def test_wrong_values(self):
        # x too small
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          692000, 184970, 0, 0)
        # x too big
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          834000, 184970, 0, 0)
        # y too small
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          740020, 114600, 0, 0)
        # y too big
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          740020, 215000, 0, 0)
        # azimut too small
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          740020, 184970, -1, 0)
        # azimut too big
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          740020, 184970, 361, 0)
        # angle too small
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          740020, 184970, 0, -1)
        # angle too big
        self.assertRaises(ValueError,
                          self.runner.calculate,
                          740020, 184970, 0, 91)

    def test_wrong_query(self):
        self.runner.calculate(740020, 184970, 0, 0)
        #fake an invalid query
        self.runner.center_x = 0
        self.assertRaises(RuntimeError, self.runner.get_values)

        self.runner.table_name = 'WRONG_NAME'
        self.assertRaises((OperationalError, ProgrammingError),
                          self.runner.calculate,
                          740020, 184970, 0, 0)

    def _run_calculation_test(self, x, y, azimut, angle, expected_result):
        self.assertEqual(
            self.runner.calculate(x, y, azimut, angle),
            expected_result)

if __name__ == '__main__':
    unittest.main()