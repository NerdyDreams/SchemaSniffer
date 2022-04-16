import unittest
from main import dictOutput

from main import SchemaSniffer


class SchemaTestCase(unittest.TestCase):
    """Tests for 'main.py' ."""

    def test_first_data(self):
        """Does it it work for data_1.json?"""
        schemaSniffer = SchemaSniffer("data/data_1.json")
        self.assertDictEqual(schemaSniffer, dictOutput, "True")

