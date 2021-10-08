from typing import List


class Person:
    def __init__(self, name: str, craft: str):
        self.name = name
        self.craft = craft


def _raise_if_tag_not_in_response(tag, json_response):
    if tag not in json_response:
        raise InvalidDocument(json_response, tag)


class CrewResponse:
    MESSAGE_TAG = 'message'
    NUMBER_TAG = 'number'
    PEOPLE_TAG = 'people'
    NAME_TAG = 'name'
    CRAFT_TAG = 'craft'

    def __init__(self, json_response):
        _raise_if_tag_not_in_response(CrewResponse.MESSAGE_TAG, json_response)
        _raise_if_tag_not_in_response(CrewResponse.NUMBER_TAG, json_response)
        _raise_if_tag_not_in_response(CrewResponse.PEOPLE_TAG, json_response)

        message = json_response[CrewResponse.MESSAGE_TAG]
        number = json_response[CrewResponse.NUMBER_TAG]

        self.message: str = message
        self.number: int = number
        self.people_list: List[Person] = []

        people = json_response[CrewResponse.PEOPLE_TAG]
        for p in people:
            _raise_if_tag_not_in_response(CrewResponse.NAME_TAG, p)
            _raise_if_tag_not_in_response(CrewResponse.CRAFT_TAG, p)

            name = p[CrewResponse.NAME_TAG]
            craft = p[CrewResponse.CRAFT_TAG]

            self.people_list.append(Person(name, craft))

    def get_people_by_craft(self) -> List[Person]:
        people_list = sorted(self.people_list, key=lambda p: p.craft)
        return people_list


class InvalidDocument(Exception):
    def __init__(self, json_response, missing_field):
        self.json_response = json_response
        self.missing_field = missing_field
