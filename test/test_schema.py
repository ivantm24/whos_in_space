from unittest import TestCase

from schema import CrewResponse


class CrewResponseTest(TestCase):

    def test_grouping(self):
        res = CrewResponse({
            CrewResponse.MESSAGE_TAG: 'success',
            CrewResponse.NUMBER_TAG: 3,
            CrewResponse.PEOPLE_TAG: [
                {CrewResponse.NAME_TAG: 'Ivan Tactuk Mercado', CrewResponse.CRAFT_TAG: 'DR'},
                {CrewResponse.NAME_TAG: 'Michael', CrewResponse.CRAFT_TAG: 'CMM'},
                {CrewResponse.NAME_TAG: 'Andre', CrewResponse.CRAFT_TAG: 'CMM'},
                {CrewResponse.NAME_TAG: 'Mark Blair', CrewResponse.CRAFT_TAG: 'DR'},
                {CrewResponse.NAME_TAG: 'Khant', CrewResponse.CRAFT_TAG: 'Myanmar'},
            ]
        })
        peoples_list = res.get_people_by_craft()

        self.assertEqual('Michael', peoples_list[0].name)
        self.assertEqual('CMM', peoples_list[0].craft)

        self.assertEqual('Andre', peoples_list[1].name)
        self.assertEqual('CMM', peoples_list[1].craft)

        self.assertEqual('Ivan Tactuk Mercado', peoples_list[2].name)
        self.assertEqual('DR', peoples_list[2].craft)

        self.assertEqual('Mark Blair', peoples_list[3].name)
        self.assertEqual('DR', peoples_list[3].craft)

        self.assertEqual('Khant', peoples_list[4].name)
        self.assertEqual('Myanmar', peoples_list[4].craft)
