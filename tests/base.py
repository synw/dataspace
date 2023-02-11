import os
import unittest
from io import StringIO
from contextlib import redirect_stdout


class BaseDsTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def _assertPrint(self, contains, expected, func, *args, **kwargs):
        f = StringIO()
        with redirect_stdout(f):
            func(*args, **kwargs)
        displayed = f.getvalue()
        if contains is True:
            self.assertIn(expected, displayed)
        else:
            self.assertEqual(displayed, expected)
