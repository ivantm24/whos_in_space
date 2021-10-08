from unittest import TestCase

from printer import CliPrinter
from schema import CrewResponse


class PrinterTest(TestCase):

    def test_max_width(self):
        res = CrewResponse({
            CrewResponse.MESSAGE_TAG: 'success',
            CrewResponse.NUMBER_TAG: 3,
            CrewResponse.PEOPLE_TAG: [
                {CrewResponse.NAME_TAG: 'Ivan Tactuk Mercado', CrewResponse.CRAFT_TAG: 'DR'},
                {CrewResponse.NAME_TAG: 'Michael', CrewResponse.CRAFT_TAG: 'DR'},
                {CrewResponse.NAME_TAG: 'Andre', CrewResponse.CRAFT_TAG: 'DR'},
            ]
        })
        self.assertEqual(
            '''Name      | Craft
----------|------
Ivan Tactu| DR   
Michael   | DR   
Andre     | DR   
''',
            CliPrinter(res, max_header_width=10).get_table()
        )
