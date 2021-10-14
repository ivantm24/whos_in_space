from unittest import TestCase

from schema import CrewResponse, Person


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

    def test_sort_by_last_name(self):
        res = CrewResponse({
            CrewResponse.MESSAGE_TAG: 'success',
            CrewResponse.NUMBER_TAG: 3,
            CrewResponse.PEOPLE_TAG: [
                {CrewResponse.NAME_TAG: 'Ivan Tactuk Mercado', CrewResponse.CRAFT_TAG: 'DR'},  # 3
                {CrewResponse.NAME_TAG: 'Michael', CrewResponse.CRAFT_TAG: 'CMM'},  # 4
                {CrewResponse.NAME_TAG: 'Andre', CrewResponse.CRAFT_TAG: 'CMM'},  # 1
                {CrewResponse.NAME_TAG: 'Mark Blair', CrewResponse.CRAFT_TAG: 'DR'},  # 2
                {CrewResponse.NAME_TAG: 'Khant Bolton Mike Act', CrewResponse.CRAFT_TAG: 'Myanmar'},  # 5
            ]
        })
        peoples_list = res.get_people_by_last_name()

        self.assertEqual('Andre', peoples_list[0].name)
        self.assertEqual('CMM', peoples_list[0].craft)

        self.assertEqual('Mark Blair', peoples_list[1].name)
        self.assertEqual('DR', peoples_list[1].craft)

        self.assertEqual('Ivan Tactuk Mercado', peoples_list[2].name)
        self.assertEqual('DR', peoples_list[2].craft)

        self.assertEqual('Michael', peoples_list[3].name)
        self.assertEqual('CMM', peoples_list[3].craft)

        self.assertEqual('Khant Bolton Mike Act', peoples_list[4].name)
        self.assertEqual('Myanmar', peoples_list[4].craft)

    def test_sort_by_last_name_descending(self):
        res = CrewResponse({
            CrewResponse.MESSAGE_TAG: 'success',
            CrewResponse.NUMBER_TAG: 3,
            CrewResponse.PEOPLE_TAG: [
                {CrewResponse.NAME_TAG: 'Ivan Tactuk Mercado', CrewResponse.CRAFT_TAG: 'DR'},  # 3
                {CrewResponse.NAME_TAG: 'Michael', CrewResponse.CRAFT_TAG: 'CMM'},  # 4
                {CrewResponse.NAME_TAG: 'Andre', CrewResponse.CRAFT_TAG: 'CMM'},  # 1
                {CrewResponse.NAME_TAG: 'Mark Blair', CrewResponse.CRAFT_TAG: 'DR'},  # 2
                {CrewResponse.NAME_TAG: 'Khant Bolton Mike Act', CrewResponse.CRAFT_TAG: 'Myanmar'},  # 5
            ]
        })
        peoples_list = res.get_people_by_last_name(ascending=False)

        self.assertEqual('Andre', peoples_list[4].name)
        self.assertEqual('CMM', peoples_list[4].craft)

        self.assertEqual('Mark Blair', peoples_list[3].name)
        self.assertEqual('DR', peoples_list[3].craft)

        self.assertEqual('Ivan Tactuk Mercado', peoples_list[2].name)
        self.assertEqual('DR', peoples_list[2].craft)

        self.assertEqual('Michael', peoples_list[1].name)
        self.assertEqual('CMM', peoples_list[1].craft)

        self.assertEqual('Khant Bolton Mike Act', peoples_list[0].name)
        self.assertEqual('Myanmar', peoples_list[0].craft)


class PersonTest(TestCase):

    def test_last_name_1(self):
        p = Person(name="Ivan", craft="ISR")
        self.assertEqual('Ivan', p.get_last_name())

    def test_last_name_2(self):
        p = Person(name="Ivan Tactuk", craft="ISR")
        self.assertEqual('Tactuk', p.get_last_name())

    def test_last_name_3(self):
        p = Person(name="Ivan Tactuk Mercado", craft="ISR")
        self.assertEqual('Mercado', p.get_last_name())

    def test_last_name_4(self):
        p = Person(name="Ivan Jose Tactuk Mercado", craft="ISR")
        self.assertEqual('Tactuk Mercado', p.get_last_name())

    def test_last_name_5(self):
        p = Person(name="Ivan Jose Maria Tactuk Mercado", craft="ISR")
        self.assertEqual('Tactuk Mercado', p.get_last_name())
