from unittest import TestCase, mock
from unittest.mock import patch

from schema import CrewResponse, InvalidDocument
from service import SpaceService, InvalidStatusCode

TEST_URL = 'test_url'
TEST_PATH = 'test_path'


def _get_mocked_connection(status: int, content):
    mocked_response = mock.Mock()
    mocked_response.getcode.return_value = status
    mocked_response.read.return_value = content
    mocked_connection = mock.Mock()
    mocked_connection.getresponse.return_value = mocked_response
    return mocked_connection


class SpaceServiceTest(TestCase):

    @patch('service.http.client.HTTPConnection')
    def test_success(self, http_con_mock):

        # mock request
        mocked_conn = _get_mocked_connection(
            200, b'{"message": "success", "number": 1, "people": [{"name":"ivan", "craft":"DR"}]}'
        )
        http_con_mock.return_value = mocked_conn

        # execute request
        res = SpaceService(TEST_URL, TEST_PATH).get_crews()

        # validate http url, path and method
        mocked_conn.request.assert_called_with('GET', TEST_PATH)
        http_con_mock.assert_called_with(TEST_URL)

        # validate response
        self.assertEqual("success", res.message)
        self.assertEqual(1, res.number)
        self.assertEqual("ivan", res.people_list[0].name)
        self.assertEqual("DR", res.people_list[0].craft)

    @patch('service.http.client.HTTPConnection')
    def test_bad_status(self, http_con_mock):

        # mock request
        mocked_conn = _get_mocked_connection(
            400, b'{"message": "success", "number": 1, "people": [{"name":"ivan", "craft":"DR"}]}'
        )
        http_con_mock.return_value = mocked_conn

        # validate raises exception
        with self.assertRaises(InvalidStatusCode) as context:
            SpaceService(TEST_URL, TEST_PATH).get_crews()

        # validate http url, path and method
        mocked_conn.request.assert_called_with('GET', TEST_PATH)
        http_con_mock.assert_called_with(TEST_URL)

        # validate exception status code
        self.assertEqual(400, context.exception.status_code)

    @patch('service.http.client.HTTPConnection')
    def test_invalid_doc(self, http_con_mock):
        # mock request
        mocked_conn = _get_mocked_connection(
            200, b'{"message": "invalid", "number": 1}'
        )
        http_con_mock.return_value = mocked_conn

        # validate raises exception
        with self.assertRaises(InvalidDocument) as context:
            SpaceService(TEST_URL, TEST_PATH).get_crews()

        # validate http url, path and method
        mocked_conn.request.assert_called_with('GET', TEST_PATH)
        http_con_mock.assert_called_with(TEST_URL)

        # validate exception status code
        self.assertEqual(CrewResponse.PEOPLE_TAG, context.exception.missing_field)
