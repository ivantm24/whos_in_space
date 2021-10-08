import http.client
import json

from schema import CrewResponse


class InvalidStatusCode(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


class SpaceService:
    def __init__(self, url="api.open-notify.org", path="/astros.json"):
        self.url = url
        self.path = path

    def get_crews(self) -> CrewResponse:
        """
        :raises http.client.HTTPException, schema.InvalidDocument, json.decoder.JSONDecodeError,
        service.InvalidStatusCode
        :return:
        """
        connection = http.client.HTTPConnection(self.url)
        connection.request("GET", self.path)
        response = connection.getresponse()
        status_code = response.getcode()
        if status_code != 200:
            raise InvalidStatusCode(status_code)
        str_response = response.read().decode()
        connection.close()

        json_response = json.loads(str_response)
        return CrewResponse(json_response)
